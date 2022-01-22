import sys
from Asisstant import Asisstant , Commands
from Sorter import Sorter


def main():
    jarvis = Asisstant()
    main_commands = Commands()
    user_commands = {
        "add contact": jarvis.add_contact,
        "show contacts": main_commands.show_commands,
        "add note": jarvis.add_note,
        "show notes": main_commands.show_notes,
    }
    user_commands_with_arguments = {
        "find contact": jarvis.find_contact,
        "add phone": jarvis.add_phone,
        "change contact": jarvis.change_contact,
        "delete contact": jarvis.del_contact,
        "get birthdays": jarvis.get_birthdays,
        "sort folder": Sorter().sort,
        "find note": jarvis.find_note,
        "tag note": jarvis.note_book.find_by_tag,
        "change note": jarvis.change_note,
        "delete note": jarvis.delete_note,
        "add tags": jarvis.add_tags,
    }
    commands = sys.argv[1:]
    str_cmd = " ".join(commands)
    if len(sys.argv) == 1:
        print(
            main_commands.show_commands()
        )
    elif len(commands) == 2:
        if str_cmd in user_commands.keys():
            user_commands.get(str_cmd)()
        else:
            print(f"I do not support this command {str_cmd}")
    elif len(commands) == 3:

        str_cmd = " ".join(commands[0:2])
        user_argument = commands[-1]

        if str_cmd in user_commands_with_arguments.keys():
            user_commands_with_arguments.get(str_cmd)(user_argument)
        else:
            print(f"I do not support this command {str_cmd}")
    else:
        print("Unknown command usage.")


if __name__ == "__main__":
    main()
