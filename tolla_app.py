import string
import logging

from kivymd.app import MDApp
from kivymd.uix.dialog import (
    MDDialog, 
    MDDialogButtonContainer, 
    MDDialogHeadlineText,
    MDDialogContentContainer
)
from kivymd.uix.widget import MDWidget
from kivymd.uix.list import (
    MDList, 
    MDListItem, 
    MDListItemHeadlineText,
    MDListItemTrailingCheckbox
)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.properties import NumericProperty, StringProperty


class TollaApp(MDApp):
    shaft_tolerance_range_letter = StringProperty()
    shaft_tolerance_range_number = NumericProperty()

    def build(self) -> None:
        super().build()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Ghostwhite"

    def open_shaft_tolerance_range_letters_menu(self):
        tolerance_range_letters = list(string.ascii_lowercase)
        tolerance_range_letters.remove("i")
        tolerance_range_letters.remove("l")
        tolerance_range_letters.remove("o")
        tolerance_range_letters.remove("q")
        tolerance_range_letters.remove("w")
        tolerance_range_letters.insert(8, "js")

        dialog = MDDialog(
            MDDialogHeadlineText(text="Выберите букву поля допуска"),
            MDDialogContentContainer(
                MDList(
                    *(
                        MDListItem(
                            MDListItemHeadlineText(text=letter),
                            MDListItemTrailingCheckbox(
                                group="shaft tolerance range letters",
                                on_press=lambda _: self.change_shaft_tolerance_range_letter(letter)
                            ),
                    ) for letter in tolerance_range_letters),
                ),
                orientation="vertical",
            ),
            MDDialogButtonContainer(
                MDWidget(),
                MDButton(
                    MDButtonText(text="Close"),
                    style="text",
                    on_press=lambda _: dialog.dismiss(),
                ),
            )
        )

        dialog.open()

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
                                    group="shaft tolerance range numbers"
                                ),
                            ) for number in shaft_tolerance_range_numbers
                        )
                    )
                )
            ).open()
        else:
            logging.error("Incorrect shaft tolerance range")

    def change_shaft_tolerance_range_letter(self, 
            shaft_tolerance_range_letter: str) -> None:
        self.shaft_tolerance_range_letter = shaft_tolerance_range_letter

