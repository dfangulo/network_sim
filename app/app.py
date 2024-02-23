from .menu import Menu


class App:
    def __init__(self) -> None:
        self.menu = Menu()
        self.view()

    def view(self) -> None:
        while True:
            sub_menu = self.menu.input_menu()
            if sub_menu == "exit":
                print(f"Saliendo del {self.menu.current_page.head}")
                break
            elif sub_menu == "return":
                self.menu.update_page_menu(self.menu.before_page.menu_name)
            else:
                try:
                    self.menu.call_menu(option=sub_menu)
                except:
                    self.menu.update_page_menu(page_menu=sub_menu)
