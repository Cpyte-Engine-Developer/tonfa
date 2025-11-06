import re

from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp
from isofits import *


BITCOIN_ADDRESS = "bc1que9qgu3d28cqhv40lq8ccr8yt80ze9h72qj6pj"
ETHERIUM_ADDRESS = "0x6dc230D8877863293E3892cB89E09432270309A0"
SOLANA_ADDRESS = "5yGJjHcLbVe81Aggfuuc6VGCeNVMdAsoGzeMjdFdWHKX"


class TonfaApp(MDApp):
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
            MDSnackbarText(text="Адрес скопирован!")
        ).open()

    def copy_etherium_address(self) -> None:
        Clipboard.copy(ETHERIUM_ADDRESS)
        
        MDSnackbar(
            MDSnackbarText(text="Адрес скопирован!")
        ).open()

    def copy_solana_address(self) -> None:
        Clipboard.copy(SOLANA_ADDRESS)

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

