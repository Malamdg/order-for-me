from Picker import Picker


def main():
    choices = [
        "1",
        "2",
        "3",
        "4"
    ]
    picker = Picker(choices)

    choice = picker.pick()
    print(choice, "has been chosen")

    picker.display_stats()


if __name__ == '__main__':
    main()
