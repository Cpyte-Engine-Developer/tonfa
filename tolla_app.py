import string
from functools import partial

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu


class TollaApp(MDApp):
    def build(self) -> None:
        super().build()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Ghostwhite"

    def open_shaft_tolerance_range_letters_menu(self, item):
        tolerance_range_letters = list(string.ascii_lowercase)
        tolerance_range_letters.remove("i")
        tolerance_range_letters.remove("l")
        tolerance_range_letters.remove("o")
        tolerance_range_letters.remove("q")
        tolerance_range_letters.remove("w")
        tolerance_range_letters.insert(8, "js")

        menu_items = [
            {
                "text": letters,
                "on_release": partial(self.on_menu_item_release, letters)
            } for letters in tolerance_range_letters
        ]
        MDDropdownMenu(caller=item, items=menu_items).open()

    def on_menu_item_release(self, letters):
        self.root.ids.shaft_tolerance_range_letters_text.text = letters
        # print(letters)

