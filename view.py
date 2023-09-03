import text


# main_menu() - Функция для распечатки нашего меню
def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f"\t{i}.{item}")
    while True:
        choise = input(text.input_menu)
        if choise.isdigit() and 0 < int(choise) < len(text.menu):
            return int(choise)
        else:
            print(text.input_menu_error)


def print_message(msg: str):
    print("\n" + "=" * len(msg))
    print(msg)
    print("=" * len(msg) + "\n")


def show_book(book: dict[int, list[str]], msg: str):
    if book:
        print("\n" + "*" * 63)
        for i, contact in book.items():
            print(
                f"{i:>3}. {contact[0]:<10} {contact[1]:<15} {contact[2]:<10} {contact[3]:<10}"
            )
        print("*" * 63 + "\n")
    else:
        print_message(msg)


def input_contact(msg: str) -> list[str]:
    contact = []
    for input_text in msg:
        contact.append(input(input_text))
    return contact


def input_request(msg: str) -> str:
    return input(msg)
