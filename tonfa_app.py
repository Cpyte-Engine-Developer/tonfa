import re
import sqlite3

from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp


BITCOIN_ADDRESS = "bc1que9qgu3d28cqhv40lq8ccr8yt80ze9h72qj6pj"
ETHERIUM_ADDRESS = "0x6dc230D8877863293E3892cB89E09432270309A0"
SOLANA_ADDRESS = "5yGJjHcLbVe81Aggfuuc6VGCeNVMdAsoGzeMjdFdWHKX"


class TonfaApp(MDApp):
    shaft_db_conn = sqlite3.connect("shaft/db/limit_deviations.db")
    hole_db_conn = sqlite3.connect("hole/db/limit_deviations.db")

    shaft_db_cur = shaft_db_conn.cursor()
    hole_db_cur = hole_db_conn.cursor()

    sql_getting_limit_deviations_code = """
        SELECT * FROM 
        (
            SELECT {tolerance_range_text}
            FROM {tolerance_range_letters}
            WHERE {diameter} <= limit_deviation 
            LIMIT 1
        )
        UNION ALL
        SELECT * FROM (
            SELECT {tolerance_range_text}
            FROM {tolerance_range_letters}
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

    def copy_bitcoin_address(self) -> None:
        Clipboard.copy(BITCOIN_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!"),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20)
        ).open()

    def copy_etherium_address(self) -> None:
        Clipboard.copy(ETHERIUM_ADDRESS)
        
        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!"),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20)
        ).open()

    def copy_solana_address(self) -> None:
        Clipboard.copy(SOLANA_ADDRESS)

        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!"),
            pos=("10dp", "10dp"),
            size_hint_x=None,
            width=self.root.width - dp(20)
        ).open()

    def fill_labels(self) -> None:
        shaft_diameter = float(self.root.ids.shaft_diameter_text_field.text)
        shaft_tolerance_range_text = self.root.ids.shaft_tolerance_range_text_field.text 

        upper_shaft_deflection_label = self.root.ids.upper_shaft_deflection_label
        lower_shaft_deflection_label = self.root.ids.lower_shaft_deflection_label
        shaft_tolerance_label = self.root.ids.shaft_tolerance_label

        try:
            shaft_tolerance_range_letters = re.match(
                r"[a-z]|js", 
                shaft_tolerance_range_text
            )[0]

            # TODO: add checking Nones
            # TODO: values less than 0 work not correctly
            shaft_limit_deviations = self.shaft_db_cur.execute(
                self.sql_getting_limit_deviations_code.format
                (
                    tolerance_range_text=shaft_tolerance_range_text, 
                    tolerance_range_letters=shaft_tolerance_range_letters,
                    diameter=shaft_diameter,
                )
            ).fetchall()
            shaft_limit_deviations = list(map(lambda x: x[0], shaft_limit_deviations))
            shaft_limit_deviations.sort()
            print(shaft_limit_deviations)

            upper_shaft_deflection_label.text = str(shaft_limit_deviations[1])
            lower_shaft_deflection_label.text = str(shaft_limit_deviations[0])
            shaft_tolerance_label.text = str(shaft_limit_deviations[1] - shaft_limit_deviations[0])
        except TypeError:
            MDSnackbar(
                MDSnackbarText(
                    text=f"Для размера {shaft_diameter} не существует поля" +
                    f" допуска {shaft_tolerance_range_text}"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20)
            ).open()

            return None
        except ZeroDivisionError:
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска вала!"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20)
            ).open()

            return None
        
        hole_diameter = float(self.root.ids.hole_diameter_text_field.text)
        hole_tolerance_range_text = self.root.ids.hole_tolerance_range_text_field.text

        upper_hole_deflection_label = self.root.ids.upper_hole_deflection_label
        lower_hole_deflection_label = self.root.ids.lower_hole_deflection_label
        hole_tolerance_label = self.root.ids.hole_tolerance_label

        try:
            hole_tolerance_range_letters = re.match(
                r"[A-Z]|JS",
                hole_tolerance_range_text
            )[0]
        
            # TODO: add checking Nones
            # TODO: values less than 0 work not correctly
            hole_limit_deviations = self.hole_db_cur.execute(
                self.sql_getting_limit_deviations_code.format
                (
                    tolerance_range_text=hole_tolerance_range_text,
                    tolerance_range_letters=hole_tolerance_range_letters,
                    diameter=hole_diameter,
                )
            ).fetchall()
            hole_limit_deviations = list(map(lambda x: x[0], hole_limit_deviations))
            hole_limit_deviations.sort()
            print(hole_limit_deviations)

            upper_hole_deflection_label.text = str(hole_limit_deviations[1])
            lower_hole_deflection_label.text = str(hole_limit_deviations[0])
            hole_tolerance_label.text = str(hole_limit_deviations[1] - hole_limit_deviations[0])
        except TypeError:
            MDSnackbar(
                MDSnackbarText(
                    text=f"Для размера {hole_diameter} не существует поля" +
                    f" допуска {hole_tolerance_range_text}"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20)
            ).open()

            return None
        except ZeroDivisionError:
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска отверстия!"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20)
            ).open()

            return None

        maximum_guaranteed_clearance_label = self.root.ids.maximum_guaranteed_clearance_label
        minimum_guaranteed_clearance_label = self.root.ids.minimum_guaranteed_clearance_label
        fit_label = self.root.ids.fit_label 
        fit_system_label = self.root.ids.fit_system_label

        maximum_guaranteed_clearance_label.text = str(hole_limit_deviations[1] - shaft_limit_deviations[0])
        minimum_guaranteed_clearance_label.text = str(hole_limit_deviations[0] - shaft_limit_deviations[1])

        if shaft_limit_deviations[0] > hole_limit_deviations[1]:
            fit_label.text = "Натяг"
        elif shaft_limit_deviations[1] > hole_limit_deviations[0]:
            fit_label.text = "Зазор"
        else:
            fit_label.text = "Переходная посадка"

        if shaft_tolerance_range_text.startswith("h") and hole_tolerance_range_text.startswith("H"):
            fit_system_label.text = "Комбинированная посадка"
        if shaft_tolerance_range_text.startswith("h"):
            fit_system_label.text = "Вал"
        if hole_tolerance_range_text.startswith("H"):
            fit_system_label.text = "Отверстие"
        else:
            fit_system_label.text = "Комбинированная посадка"

