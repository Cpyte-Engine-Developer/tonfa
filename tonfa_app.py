from functools import partial
import logging
import re
import string

from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogButtonContainer,
    MDDialogContentContainer,
    MDDialogHeadlineText,
)
from kivymd.uix.dropdownitem import MDDropDownItem, MDDropDownItemText
from kivymd.uix.list import (
    MDList,
    MDListItem,
    MDListItemHeadlineText,
    MDListItemTrailingCheckbox,
)
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.widget import MDWidget


class TonfaApp(MDApp):
    shaft_tolerance_range_letter = StringProperty()
    shaft_tolerance_range_number = NumericProperty()
    hole_tolerance_range_letter = StringProperty()
    hole_tolerance_range_number = NumericProperty()

    def build(self) -> None:
        super().build()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Ghostwhite"

    def validate_shaft_tolerance_range(self, text_input: str) -> None:
        # this regular expression check that text input is correct tolerance range
        if re.fullmatch(
                r"(a(9|1[0-3]))|(b([8-9]|1[0-3]))|(c([8-9]|1[0-2]))|"
                r"(d([5-9]|1[0-3]))|(e([5-9]|10))|(f([3-9]|10))|(g([3-9]|10))|"
                r"(h([1-9]|1[0-8]))|(js([1-9]|1[0-8]))|(j[5-8])|"
                r"(k([3-9]|1[0-3]))|(m[3-9])|(n[3-9])|(p([3-9]|10]))|"
                r"(r([3-9]|10))|(s([3-9]|10))|(t[5-8])|(u[5-9])|(v[5-8])|"
                r"(x([5-9]|10))|(y([6-9]|10))|(z([6-9]|1[0-1]))",
                text_input
                ) is None:
            MDSnackbar(
                MDSnackbarText(text="Неправильное поле допуска вала")
            ).open()
        else:
            text_input_letters = re.match(r"[a-z]|js", text_input)
            text_input_number = re.search(r"[1-9]\d", text_input)

            print(text_input_letters, text_input_number)

    def open_shaft_tolerance_range_letters_menu(self) -> None:
        tolerance_range_letters = list(string.ascii_lowercase)
        tolerance_range_letters.remove("i")
        tolerance_range_letters.remove("l")
        tolerance_range_letters.remove("o")
        tolerance_range_letters.remove("q")
        tolerance_range_letters.remove("w")
        tolerance_range_letters.insert(8, "js")

        menu_items = (
            {
                "text": letter,
                "on_release": partial(
                    lambda letter: self.set_shaft_tolerance_range_menu_item(
                        letter
                    ),
                    letter=letter,
                ),
            }
            for letter in tolerance_range_letters
        )

        self.menu = MDDropdownMenu(
            caller=self.root.ids.shaft_tolerance_range_letters_text_field,
            items=menu_items,
            position="bottom",
        )
        self.menu.open()

    def set_shaft_tolerance_range_menu_item(self, letter: str) -> None:
        self.root.ids.shaft_tolerance_range_letters_text_field.text = letter
        self.menu.dismiss()

    def open_shaft_tolerance_range_numbers_menu(self):
        shaft_tolerance_range_numbers = None

        match self.shaft_tolerance_range_letter:
            case "a":
                shaft_tolerance_range_numbers = range(9, 14)
            case "b":
                shaft_tolerance_range_numbers = range(8, 14)
            case "c":
                shaft_tolerance_range_numbers = range(8, 13)
            case "d":
                shaft_tolerance_range_numbers = range(5, 14)
            case "e":
                shaft_tolerance_range_numbers = range(5, 11)
            case "f":
                shaft_tolerance_range_numbers = range(3, 11)
            case "g":
                shaft_tolerance_range_numbers = range(3, 11)
            case "h":
                shaft_tolerance_range_numbers = range(1, 19)
            case "js":
                shaft_tolerance_range_numbers = range(1, 19)
            case "j":
                shaft_tolerance_range_numbers = range(5, 9)
            case "k":
                shaft_tolerance_range_numbers = range(3, 14)
            case "m":
                shaft_tolerance_range_numbers = range(3, 10)
            case "n":
                shaft_tolerance_range_numbers = range(3, 10)
            case "p":
                shaft_tolerance_range_numbers = range(3, 11)
            case "r":
                shaft_tolerance_range_numbers = range(3, 11)
            case "s":
                shaft_tolerance_range_numbers = range(3, 11)
            case "t":
                shaft_tolerance_range_numbers = range(5, 9)
            case "u":
                shaft_tolerance_range_numbers = range(5, 10)
            case "v":
                shaft_tolerance_range_numbers = range(5, 9)
            case "x":
                shaft_tolerance_range_numbers = range(5, 11)
            case "y":
                shaft_tolerance_range_numbers = range(6, 11)
            case "z":
                shaft_tolerance_range_numbers = range(6, 12)
            case letter:
                logging.error(f"Incorrect letter. Current letter is {letter}")

        if shaft_tolerance_range_numbers is not None:
            MDDialog(
                MDDialogHeadlineText(text="Выберите число поля допуска"),
                MDDialogContentContainer(
                    MDList(
                        *(
                            MDListItem(
                                MDListItemHeadlineText(text=str(number)),
                                MDListItemTrailingCheckbox(
                                    group="shaft tolerance range numbers",
                                    on_press=lambda _: self.change_shaft_tolerance_range_number(
                                        number
                                    ),
                                ),
                            )
                            for number in shaft_tolerance_range_numbers
                        )
                    )
                ),
            ).open()
        else:
            logging.error("Incorrect shaft tolerance range")

    def change_shaft_tolerance_range_letter(
        self, shaft_tolerance_range_letter: str
    ) -> None:
        self.shaft_tolerance_range_letter = shaft_tolerance_range_letter

    def change_shaft_tolerance_range_number(
        self, shaft_tolerance_range_number: float
    ) -> None:
        self.shaft_tolerance_range_number = shaft_tolerance_range_number

    def open_hole_tolerance_range_letters_menu(self) -> None:
        tolerance_range_letters = list(string.ascii_uppercase)
        tolerance_range_letters.remove("I")
        tolerance_range_letters.remove("L")
        tolerance_range_letters.remove("O")
        tolerance_range_letters.remove("Q")
        tolerance_range_letters.remove("W")
        tolerance_range_letters.insert(8, "JS")

        dialog = MDDialog(
            MDDialogHeadlineText(text="Выберите букву поля допуска"),
            MDDialogContentContainer(
                MDList(
                    *(
                        MDListItem(
                            MDListItemHeadlineText(text=letter),
                            MDListItemTrailingCheckbox(
                                group="shaft tolerance range letters",
                                on_press=lambda _: self.change_hole_tolerance_range_letter(
                                    letter
                                ),
                            ),
                        )
                        for letter in tolerance_range_letters
                    ),
                ),
                orientation="vertical",
            ),
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(
                    MDButtonText(text="Закрыть"),
                    style="text",
                    on_press=lambda _: dialog.dismiss(),
                ),
            ),
        )

        dialog.open()

    def open_hole_tolerance_range_numbers_menu(self):
        hole_tolerance_range_numbers = None

        match self.hole_tolerance_range_letter:
            case "A":
                hole_tolerance_range_numbers = range(9, 14)
            case "B":
                hole_tolerance_range_numbers = range(8, 14)
            case "C":
                hole_tolerance_range_numbers = range(8, 13)
            case "D":
                hole_tolerance_range_numbers = range(5, 14)
            case "E":
                hole_tolerance_range_numbers = range(5, 11)
            case "F":
                hole_tolerance_range_numbers = range(3, 11)
            case "G":
                hole_tolerance_range_numbers = range(3, 11)
            case "H":
                hole_tolerance_range_numbers = range(1, 19)
            case "JS":
                hole_tolerance_range_numbers = range(1, 19)
            case "J":
                hole_tolerance_range_numbers = range(5, 9)
            case "K":
                hole_tolerance_range_numbers = range(3, 14)
            case "M":
                hole_tolerance_range_numbers = range(3, 10)
            case "N":
                hole_tolerance_range_numbers = range(3, 10)
            case "P":
                hole_tolerance_range_numbers = range(3, 11)
            case "R":
                hole_tolerance_range_numbers = range(3, 11)
            case "S":
                hole_tolerance_range_numbers = range(3, 11)
            case "T":
                hole_tolerance_range_numbers = range(5, 9)
            case "U":
                hole_tolerance_range_numbers = range(5, 10)
            case "V":
                hole_tolerance_range_numbers = range(5, 9)
            case "X":
                hole_tolerance_range_numbers = range(5, 11)
            case "Y":
                hole_tolerance_range_numbers = range(6, 11)
            case "Z":
                hole_tolerance_range_numbers = range(6, 12)
            case letter:
                logging.error(f"Incorrect letter. Current letter is {letter}")

        if hole_tolerance_range_numbers is not None:
            MDDialog(
                MDDialogHeadlineText(text="Выберите число поля допуска"),
                MDDialogContentContainer(
                    MDList(
                        *(
                            MDListItem(
                                MDListItemHeadlineText(text=str(number)),
                                MDListItemTrailingCheckbox(
                                    group="shaft tolerance range numbers",
                                    on_press=lambda _: self.change_shaft_tolerance_range_number(
                                        number
                                    ),
                                ),
                            )
                            for number in hole_tolerance_range_numbers
                        ),
                    ),
                ),
            ).open()
        else:
            logging.error("Incorrect hole tolerance range")

    def change_hole_tolerance_range_letter(
        self, hole_tolerance_range_letter: str
    ) -> None:
        self.hole_tolerance_range_letter = hole_tolerance_range_letter

    def change_hole_tolerance_range_number(
        self, hole_tolerance_range_number: float
    ) -> None:
        self.hole_tolerance_range_number = hole_tolerance_range_number
