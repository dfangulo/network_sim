from os import system
from .menu_items import menu_options


class Menu:
    def __init__(self) -> None:
        self.menu_options = menu_options
        # self.update_level_menu(level_menu="main_menu")

    def call_menu(self, option: str) -> None:
        # Intenta obtener la función correspondiente por su nombre
        func = getattr(self, option, None)
        if func:
            func()  # Llama a la función si se encontró
        else:
            print(f"La opción '{option}' no tiene una función asociada.")

    def input_menu(self) -> str:
        while True:
            system("cls")
            self.main_menu()
            answer = input("Seleciona una opçión: ").strip().lower()
            if len(answer) > 0:
                if answer in self.menu_options.get(self.level_menu):
                    return self.menu_options[self.level_menu][answer]
                else:
                    keys=[]
                    print(f"La opcion:'{answer}', no es valida","\nSeleciona alguna opcion valida:")
                    for key in self.menu_options[self.level_menu]:
                        keys.append(key)
                    print("\t",", ".join(keys))
                    input("Enter para continuar!")

    def main_menu(self) -> None:
        self.update_level_menu(level_menu="main_menu")
        menu_list = {
            "label": "Menu del Juego",
            "option1": "Menu 1",
            "option2": "Menu 2",
            "option3": "Menu 3",
            "option4": "Menu 4",
            "quit": "(Q) - Salir del Juego",
        }
        self.print_menus(menu_list=menu_list)

    def print_menus(self, menu_list) -> None:
        menu_large: int = 21
        line = ("-" * (len(menu_list["label"]) + round(menu_large / 2))).center(
            menu_large, "-"
        )
        print(
            line + "\n",
            (menu_list["label"]).center(menu_large, " "),
            "\n" + line + "\n",
        )

        for key, value in menu_list.items():
            if key == "label" or key == "quit":
                continue
            print(f"{value}")
        print(
            "\n" + line + "\n",
            (menu_list["quit"]).center(menu_large, " "),
            "\n" + line + "\n\n",
        )

    def update_level_menu(self, level_menu: str) -> None:
        self.level_menu = level_menu
