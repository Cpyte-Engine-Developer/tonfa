import re
import sqlite3
import gettext
import os
from pathlib import Path

from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogButtonContainer,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogContentContainer,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.list import (
    MDListItem,
    MDListItemSupportingText,
    MDListItemTrailingCheckbox,
)
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp
from kivy.config import Config
from kivy.logger import Logger


class TonfaApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BITCOIN_ADDRESS = "bc1que9qgu3d28cqhv40lq8ccr8yt80ze9h72qj6pj"
        self.ETHERIUM_ADDRESS = "0x6dc230D8877863293E3892cB89E09432270309A0"
        self.SOLANA_ADDRESS = "5yGJjHcLbVe81Aggfuuc6VGCeNVMdAsoGzeMjdFdWHKX"

        self.shaft_db_conn = sqlite3.connect("shaft/db/limit_deviations.db")
        self.hole_db_conn = sqlite3.connect("hole/db/limit_deviations.db")

        self.shaft_db_cur = self.shaft_db_conn.cursor()
        self.hole_db_cur = self.hole_db_conn.cursor()

        self.GETTING_LIMIT_DEVIATIONS_CODE = """
            SELECT * FROM 
            (
                SELECT {tolerance_class}
                FROM {fundamental_deviation}
                WHERE {diameter} <= diameter 
                LIMIT 1
            )
            UNION ALL
            SELECT * FROM (
                SELECT {tolerance_class}
                FROM {fundamental_deviation}
                WHERE {diameter} > diameter
                ORDER BY diameter DESC
                LIMIT 1, 1
            )
        """

        self.GETTING_MAX_DIAMETER = "SELECT MAX(diameter) from {table}"
        self.GETTING_MIN_DIAMETER = "SELECT MIN(diameter) from {table}"

        self.current_lang = Config.getdefault("tonfa", "lang", "ru")

        self.LOCALE_DIR = Path("locale/").absolute()
        LANGUAGES = os.listdir(self.LOCALE_DIR)
        if "tonfa.pot" in LANGUAGES: 
            LANGUAGES.remove("tonfa.pot")

        self.TRANSLATIONS = {
            lang: gettext.translation(
                "tonfa",
                localedir=self.LOCALE_DIR,
                languages=[lang],
                fallback=True,
            )
            for lang in LANGUAGES
        }
        self.TRANSLATIONS[self.current_lang].install()

        self.lang_dialog = MDDialog(
            MDDialogHeadlineText(
                text=_("Выберите язык"),
            ),
            MDDialogSupportingText(
                text=_("Для смены языка необходимо перезапустить приложение")
            ),
            MDDialogContentContainer(
                *(
                    MDListItem(
                        MDListItemSupportingText(
                            text=lang,
                        ),
                        MDListItemTrailingCheckbox(
                            on_active=lambda _,
                            is_selected,
                            lang=lang: self.change_language(lang, is_selected),
                            group="lang",
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    )
                    for lang in self.TRANSLATIONS
                ),
                orientation="vertical",
            ),
            MDDialogButtonContainer(
                MDButton(
                    MDButtonText(
                        text=_("OK"),
                    ),
                    style="text",
                    on_press=lambda _: self.lang_dialog.dismiss(),
                ),
            ),
        )

    def on_start(self) -> None:
        Config.adddefaultsection("tonfa")

    def build(self) -> None:
        super().build()

        self.theme_cls.theme_style = Config.getdefault("tonfa", "theme", "Dark")
        self.theme_cls.primary_palette = "Ghostwhite"

    def open_donation_screen(self) -> None:
        self.root.ids.screen_manager.current = "donation"

    def open_main_screen(self) -> None:
        self.root.ids.screen_manager.current = "main"

    def open_settings_screen(self) -> None:
        self.root.ids.screen_manager.current = "settings"

    def copy_bitcoin_address(self) -> None:
        Clipboard.copy(self.BITCOIN_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text=_("Адрес скопирован!")),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20),
        ).open()

    def copy_etherium_address(self) -> None:
        Clipboard.copy(self.ETHERIUM_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text=_("Адрес скопирован!")),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20),
        ).open()

    def copy_solana_address(self) -> None:
        Clipboard.copy(self.SOLANA_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text=_("Адрес скопирован!")),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20),
        ).open()

    def fill_labels(self) -> None:
        diameter = float(self.root.ids.diameter_text_field.text)
        shaft_tolerance_class = (
            self.root.ids.shaft_tolerance_class_text_field.text
        )

        es_label = self.root.ids.es_label
        ei_label = self.root.ids.ei_label
        shaft_tolerance_label = self.root.ids.shaft_tolerance_label

        try:
            shaft_fundamental_deviation = re.match(
                r"[a-z]|js", shaft_tolerance_class
            )[0]

            shaft_min_diameter = int(self.shaft_db_cur.execute(
                self.GETTING_MIN_DIAMETER.format(table=shaft_fundamental_deviation)
            ).fetchone()[0])
            shaft_max_diameter = int(self.shaft_db_cur.execute(
                self.GETTING_MAX_DIAMETER.format(table=shaft_fundamental_deviation)
            ).fetchone()[0])

            if diameter <= shaft_min_diameter:
                raise ValueError("Invalid diameter. Diameter must be bigger")
            elif diameter > shaft_max_diameter:
                raise ValueError("Invalid diameter. Diameter must be smaller")

            shaft_limit_deviations = self.shaft_db_cur.execute(
                self.GETTING_LIMIT_DEVIATIONS_CODE.format(
                    tolerance_class=shaft_tolerance_class,
                    fundamental_deviation=shaft_fundamental_deviation,
                    diameter=diameter,
                )
            ).fetchall()
            shaft_limit_deviations = list(
                map(lambda x: x[0], shaft_limit_deviations)
            )
            shaft_limit_deviations.sort()

            es_label.text = str(shaft_limit_deviations[1])
            ei_label.text = str(shaft_limit_deviations[0])
            shaft_tolerance_label.text = str(
                shaft_limit_deviations[1] - shaft_limit_deviations[0]
            )
        except (TypeError, sqlite3.OperationalError, ValueError) as e:
            MDSnackbar(
                MDSnackbarText(
                    text=_("Неправильный класс допуска вала или диаметр")
                ),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20),
            ).open()

            Logger.exception(e)

            return None
        except Exception as e:
            MDSnackbar(
                MDSnackbarText(
                    text=_("Непредвиденная ошибка")
                ),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20),
            ).open()
            Logger.exception(e)

            return None

        hole_tolerance_class = (
            self.root.ids.hole_tolerance_class_text_field.text
        )

        ES_label = self.root.ids.ES_label
        EI_label = self.root.ids.EI_label
        hole_tolerance_label = self.root.ids.hole_tolerance_label

        try:
            hole_fundamental_deviation = re.match(
                r"[A-Z]|JS", hole_tolerance_class
            )[0]

            hole_min_diameter = int(self.hole_db_cur.execute(
                self.GETTING_MIN_DIAMETER.format(table=hole_fundamental_deviation)
            ).fetchone()[0])
            hole_max_diameter = int(self.hole_db_cur.execute(
                self.GETTING_MAX_DIAMETER.format(table=hole_fundamental_deviation)
            ).fetchone()[0])

            if diameter <= hole_min_diameter:
                raise ValueError("Invalid diameter. Diameter must be bigger")
            elif diameter > hole_max_diameter:
                raise ValueError("Invalid diameter. Diameter must be smaller")

            hole_limit_deviations = self.hole_db_cur.execute(
                self.GETTING_LIMIT_DEVIATIONS_CODE.format(
                    tolerance_class=hole_tolerance_class,
                    fundamental_deviation=hole_fundamental_deviation,
                    diameter=diameter,
                )
            ).fetchall()
            hole_limit_deviations = list(
                map(lambda x: x[0], hole_limit_deviations)
            )
            hole_limit_deviations.sort()

            ES_label.text = str(hole_limit_deviations[1])
            EI_label.text = str(hole_limit_deviations[0])
            hole_tolerance_label.text = str(
                hole_limit_deviations[1] - hole_limit_deviations[0]
            )
        except (TypeError, sqlite3.OperationalError, ValueError) as e:
            MDSnackbar(
                MDSnackbarText(
                    text=_("Неправильный класс допуска отверстия или диаметр")
                ),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20),
            ).open()

            Logger.exception(e)

            return None
        except Exception as e:
            MDSnackbar(
                MDSnackbarText(
                    text=_("Непредвиденная ошибка")
                ),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20),
            ).open()
            Logger.exception(e)

            return None

        maximum_clearance_label = self.root.ids.maximum_clearance_label
        minimum_clearance_label = self.root.ids.minimum_clearance_label
        fit_label = self.root.ids.fit_label
        fit_system_label = self.root.ids.fit_system_label

        maximum_clearance_label.text = str(
            hole_limit_deviations[1] - shaft_limit_deviations[0]
        )
        minimum_clearance_label.text = str(
            hole_limit_deviations[0] - shaft_limit_deviations[1]
        )

        if shaft_limit_deviations[0] > hole_limit_deviations[1]:
            fit_label.text = _("Натяг")
        elif shaft_limit_deviations[1] > hole_limit_deviations[0]:
            fit_label.text = _("Зазор")
        else:
            fit_label.text = _("Переходная посадка")

        if shaft_tolerance_class.startswith(
            "h"
        ) and hole_tolerance_class.startswith("H"):
            fit_system_label.text = _("Комбинированная посадка")
        if shaft_tolerance_class.startswith("h"):
            fit_system_label.text = _("Вал")
        if hole_tolerance_class.startswith("H"):
            fit_system_label.text = _("Отверстие")
        else:
            fit_system_label.text = _("Комбинированная посадка")

    def choose_language(self) -> None:
        self.lang_dialog.open()

    def change_language(self, lang: str, is_selected: bool) -> None:
        if is_selected:
            self.current_lang = lang
            self.root.ids.lang_button_text.text = self.current_lang

            Config.set("tonfa", "lang", self.current_lang)
            Config.write()

    def change_theme(self) -> None:
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        elif self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"

        Config.set("tonfa", "theme", self.theme_cls.theme_style)
        Config.write()

    def on_stop(self) -> None:
        self.shaft_db_conn.close()
        self.hole_db_conn.close()

    def is_current_theme_light(self) -> bool:
        return Config.getdefault("tonfa", "theme", "Dark") == "Light"

