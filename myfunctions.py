class Colors:
    """Console colors"""
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


pop_it: dict[int, int] = dict()


def choose_objects(row: int, balance_objects: int) -> int:
    """This function asks the user to enter number of objects to remove from the selected row"""
    while True:
        remove_objects = get_positive_number("How many to remove?: ")
        if remove_objects > pop_it[row] or remove_objects == balance_objects:
            print("re enter a valid value")
            continue
        else:
            break
    return remove_objects


def choose_row() -> int:
    """This function asks the user to choose a row"""
    while True:
        row = get_positive_number(f"Choose the row: ")
        if row not in pop_it:
            print(f"Error: Row {row} not found!")
            print("Re-enter a valid row")
            continue
        else:
            return row


def get_positive_number(prompt: str) -> int:
    """Get integer input from user
    :param prompt:
    :return: num
    """
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a positive number.")
            else:
                return num
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(f"An error occurred: {e}")


def design_pattern() -> None:
    """Design the game pattern"""
    print(f"Let us first design a desired pattern to play :)\n")
    rows = get_positive_number("Enter number of rows:")
    objects_per_row = get_positive_number("Enter number of objects or zero to input objects row wise:")
    for key in range(rows):
        if objects_per_row != 0:
            pop_it[key+1] = objects_per_row  # range start with zero but key start with one. hence add 1
        else:
            pop_it[key+1] = get_positive_number(f"Enter number objects in row:{key + 1}\t:")


def print_pattern() -> int:
    number_of_objects = 0
    for i, j in pop_it.items():
        print("ROW:", i, "\t", j * '1 ', end="\n")
        number_of_objects += j
    return number_of_objects


def update_pattern(row: int, remove_objects: int) -> None:
    """update the dict for the row and object removal"""
    pop_it[row] -= remove_objects
    if len(pop_it) != 1 and pop_it[row] == 0:
        del pop_it[row]


def play_game(move_number: int = 0) -> None:
    """prints the pattern and check if the game is over"""

    balance_objects = print_pattern()
    if balance_objects == 1:
        print("game over, total moves:", move_number)
        return
    else:
        # print whose turn it is, player 1 or 2
        if move_number % 2:
            print(f"{Colors.CYAN}Player:2{Colors.ENDC}")
        else:
            print(f"{Colors.CYAN}Player:1{Colors.ENDC}")

    row = choose_row()
    remove_objects = choose_objects(row, balance_objects)
    update_pattern(row, remove_objects)
    play_game(move_number+1)
