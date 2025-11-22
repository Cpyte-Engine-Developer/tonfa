import re
import sqlite3

from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp


class TonfaApp(MDApp):
    BITCOIN_ADDRESS = "bc1que9qgu3d28cqhv40lq8ccr8yt80ze9h72qj6pj"
    ETHERIUM_ADDRESS = "0x6dc230D8877863293E3892cB89E09432270309A0"
    SOLANA_ADDRESS = "5yGJjHcLbVe81Aggfuuc6VGCeNVMdAsoGzeMjdFdWHKX"

    shaft_db_conn = sqlite3.connect("shaft/db/limit_deviations.db")
    hole_db_conn = sqlite3.connect("hole/db/limit_deviations.db")

    shaft_db_cur = shaft_db_conn.cursor()
    hole_db_cur = hole_db_conn.cursor()

    GETTING_LIMIT_DEVIATIONS_CODE = """
        SELECT * FROM 
        (
            SELECT {tolerance_class}
            FROM {fundamental_deviation}
            WHERE {diameter} <= limit_deviation 
            LIMIT 1
        )
        UNION ALL
        SELECT * FROM (
            SELECT {tolerance_class}
            FROM {fundamental_deviation}
            WHERE {diameter} > limit_deviation
            ORDER BY limit_deviation DESC
            LIMIT 1, 1
        )
    """

    def build(self) -> None:
        super().build()
        self.theme_cls.theme_style = "Dark"
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
            MDSnackbarText(text="Адрес скопирован!"),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20),
        ).open()

    def copy_etherium_address(self) -> None:
        Clipboard.copy(self.ETHERIUM_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!"),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20),
        ).open()

    def copy_solana_address(self) -> None:
        Clipboard.copy(self.SOLANA_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!"),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20),
        ).open()

    def fill_labels(self) -> None:
        diameter = float(self.root.ids.diameter_text_field.text)
        shaft_tolerance_class = (
            self.root.ids.shaft_tolerance_class_text_field.text
        )

        es_label = (
            self.root.ids.es_label
        )
        ei_label = (
            self.root.ids.ei_label
        )
        shaft_tolerance_label = self.root.ids.shaft_tolerance_label

        try:
            shaft_fundamental_deviation = re.match(
                r"[a-z]|js", shaft_tolerance_class
            )[0]

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
        except (TypeError, sqlite3.OperationalError):
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска или размер вала"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20),
            ).open()

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
        except (TypeError, sqlite3.OperationalError):
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска или размер отверстия"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20),
            ).open()

            return None

        maximum_clearance_label = (
            self.root.ids.maximum_clearance_label
        )
        minimum_clearance_label = (
            self.root.ids.minimum_clearance_label
        )
        fit_label = self.root.ids.fit_label
        fit_system_label = self.root.ids.fit_system_label

        maximum_clearance_label.text = str(
            hole_limit_deviations[1] - shaft_limit_deviations[0]
        )
        minimum_clearance_label.text = str(
            hole_limit_deviations[0] - shaft_limit_deviations[1]
        )

        if shaft_limit_deviations[0] > hole_limit_deviations[1]:
            fit_label.text = "Натяг"
        elif shaft_limit_deviations[1] > hole_limit_deviations[0]:
            fit_label.text = "Зазор"
        else:
            fit_label.text = "Переходная посадка"

        if shaft_tolerance_class.startswith(
            "h"
        ) and hole_tolerance_class.startswith("H"):
            fit_system_label.text = "Комбинированная посадка"
        if shaft_tolerance_class.startswith("h"):
            fit_system_label.text = "Вал"
        if hole_tolerance_class.startswith("H"):
            fit_system_label.text = "Отверстие"
        else:
            fit_system_label.text = "Комбинированная посадка"

