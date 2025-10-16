from kivymd.app import MDApp


class TollaApp(MDApp):
    def build(self) -> None:
        super().build()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Ghostwhite"
