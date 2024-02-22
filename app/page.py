class Page:
    def __init__(self, head: str, options: list, bottom: str) -> None:
        self.head = head
        self.options = options
        self.bottom = bottom
        self.large_page = 27

    def display(self):
        print("-" * self.large_page)
        print(f"{self.head.center(self.large_page)}")
        print("-" * self.large_page, 2 * "\n")

        for index, option in enumerate(self.options, start=1):
            print(f"\t{index}. {option.center(len(option))}")

        print(2 * "\n", "-" * self.large_page)
        print(f"{self.bottom.center(self.large_page)}")
        print("-" * self.large_page)
        print("\n")


if __name__ == "__main__":
    # Crear las páginas
    pagina1 = Page(
        head="Simulador de Redes",
        options=["Menu 1", "Menu 2", "Menu 3", "Menu 4"],
        bottom="Cerrar aplicación",
    )
    pagina2 = Page(
        head="Otra página",
        options=["Opción 1", "Opción 2"],
        bottom="Volver al menú principal",
    )

    # Mostrar la primera página
    pagina_actual = pagina1

    while True:
        pagina_actual.display()
        opcion = input("Seleccione una opción:").strip().lower()

        if opcion == "q":
            print("Saliendo...")
            break
        elif opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(pagina_actual.options):
                print(f"Seleccionaste la opción {pagina_actual.options[opcion - 1]}")
                # Aquí podrías implementar la lógica para manejar la opción seleccionada
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
