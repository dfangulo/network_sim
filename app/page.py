class Page:
    def __init__(
        self,
        menu_name: str,
        func_name: str,
        head: str,
        options: dict,
        options_display: list,
        bottom: str,
    ) -> None:
        self.menu_name = menu_name
        self.func_name = func_name
        self.head = head
        self.options = options
        self.options_display = options_display
        self.bottom = bottom
        self.large_page = 27

    def __str__(self) -> str:
        return f"{self.name}"

    def display(self):
        print("-" * self.large_page)
        print(f"{self.head.center(self.large_page)}")
        print("-" * self.large_page, 2 * "\n")

        for index, option in enumerate(self.options_display, start=1):
            print(f"\t{index}. {option.center(len(option))}")

        print(2 * "\n", "-" * self.large_page)
        print(f"{self.bottom.center(self.large_page)}")
        print("-" * self.large_page)
        print("\n")
