import re

from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp
from isofits import *


class TonfaApp(MDApp):
    def build(self) -> None:
        super().build()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Ghostwhite"

    def validate_shaft_tolerance_range(self, text: str) -> None:
        # this regular expression check that text input is correct tolerance range
        reg_exp = "(a(9|1[0-3]))|(b([8-9]|1[0-3]))|(c([8-9]|1[0-2]))|" + \
        "(d([5-9]|1[0-3]))|(e([5-9]|10))|(f([3-9]|10))|(g([3-9]|10))|" + \
        "(h(1[0-8]|[1-9]))|(js(1[0-8]|[1-9]))|(j[5-8])|" + \
        "(k([3-9]|1[0-3]))|(m[3-9])|(n[3-9])|(p([3-9]|10]))|" + \
        "(r([3-9]|10))|(s([3-9]|10))|(t[5-8])|(u[5-9])|(v[5-8])|" + \
        "(x([5-9]|10))|(y([6-9]|10))|(z([6-9]|1[0-1]))"

        print(re.fullmatch(reg_exp, text))
        if re.fullmatch(reg_exp, text) is None:
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска вала"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20)
            ).open()

    def validate_hole_tolerance_range(self, text: str) -> None:
        # this regular expression check that text input is correct tolerance range
        reg_exp = r"(A(9|1[0-3]))|(B([8-9]|1[0-3]))|(C([8-9]|1[0-3]))|" + \
        "(D([6-9]|1[0-3]))|(E([5-9]|10))|(F([3-9]|10))|(G([3-9]|10))|" + \
        "(H([1-9]|1[0-8]))|(JS([1-9]|1[0-8]))|(J[6-8])|(K([3-9]|10))|" + \
        "(M([3-9]|10))|(N([3-9]|1[0-1]))|(P([3-9]|10))|(R([3-9]|10))|" + \
        "(S([3-9]|10))|(T[5-8])|(U([5-9]|10))|(V[5-8])|(X([5-9]|10))|" + \
        "(Y([6-9]|10))|(Z([6-9]|1[0-1]))"

        if re.fullmatch(reg_exp, text) is None:
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска отверстия"),
                pos=("10dp", "10dp"),
                size_hint_x=None,
                width=self.root.width - dp(20)
            ).open()

    def open_donation_screen(self) -> None:
        self.root.ids.screen_manager.current = "donation"

    def open_main_screen(self) -> None:
        self.root.ids.screen_manager.current = "main"

    def copy_bitcoin_address(self) -> None:
        Clipboard.copy("bc1que9qgu3d28cqhv40lq8ccr8yt80ze9h72qj6pj")

        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!")
        ).open()

    def copy_etherium_address(self) -> None:
        Clipboard.copy("0x6dc230D8877863293E3892cB89E09432270309A0")
        
        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!")
        ).open()

    def copy_solana_address(self) -> None:
        Clipboard.copy("5yGJjHcLbVe81Aggfuuc6VGCeNVMdAsoGzeMjdFdWHKX")

        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!")
        ).open()

    def fill_labels(self) -> None:
        shaft_diameter = self.root.ids.shaft_diameter_text_field.text
        shaft_tolerance_range_text = self.root.ids.shaft_tolerance_range_text_field.text 
        upper_shaft_deflection_label = self.root.ids.upper_shaft_deflection_label
        lower_shaft_deflection_label = self.root.ids.lower_shaft_deflection_label

        shaft_tolerance_range = list(isotol("shaft", float(shaft_diameter), shaft_tolerance_range_text, "both"))
        shaft_tolerance_range[0] = shaft_tolerance_range[0] / 1000
        shaft_tolerance_range[1] = shaft_tolerance_range[1] / 1000

        hole_diameter = self.root.ids.hole_diameter_text_field.text
        hole_tolerance_range_text = self.root.ids.hole_tolerance_range_text_field.text
        upper_hole_deflection_label = self.root.ids.upper_hole_deflection_label
        lower_hole_deflection_label = self.root.ids.lower_hole_deflection_label

        hole_tolerance_range = list(isotol("hole", float(hole_diameter), hole_tolerance_range_text, "both"))
        hole_tolerance_range[0] = hole_tolerance_range[0] / 1000
        hole_tolerance_range[1] = hole_tolerance_range[1] / 1000

