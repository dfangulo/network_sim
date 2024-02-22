from os import system
from .menu_items import menu_options
from .page import Page


class Menu:
    def __init__(self) -> None:
        self.menu_options = menu_options
        self.load_pages()

    def load_pages(self) -> None:
        self.main_page = Page(
            head="Simulador de Redes",
            options=["Nueva Red", "Cargar Red"],
            bottom="(q) Cerrar aplicación",
        )
        self.new_network = Page(
            head="Nueva Red",
            options=[
                "",
                "",
                "",
                "",
            ],
            bottom="(r) Regresar",
        )

    def call_menu(self, option: str) -> None:
        # Intenta obtener la función correspondiente por su nombre
        func = getattr(self, option, None)
        if func:
            func()  # Llama a la función si se encontró
        else:
            print(f"La opción '{option}' no tiene una función asociada.")

    def input_menu(self) -> str:
        self.update_page_menu(page_menu="main_menu")
        while True:
            system("cls")
            self.main_page.display()
            answer = input("Seleciona una opçión: ").strip().lower()
            if len(answer) > 0:
                if answer in self.menu_options.get(self.page_menu):
                    return self.menu_options[self.page_menu][answer]
                else:
                    """
                    Mostrar la información de las llaves en self.page_menu
                    """
                    keys = []
                    print(
                        f"La opcion:'{answer}', no es valida",
                        "\nSeleciona alguna opcion valida:",
                    )
                    for key in self.menu_options[self.page_menu]:
                        keys.append(key)
                    print("\t", ", ".join(keys))
                    input("Enter para continuar!")

    def update_page_menu(self, page_menu: str) -> None:
        self.page_menu = page_menu
