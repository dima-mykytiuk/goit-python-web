"""Imports for main"""
from assistant import (
    add_contact,
    change_contact,
    del_contact,
    find_contact,
    get_birthdays,
    add_note,
    change_note,
    delete_note,
    find_note_by_name,
    add_tags,
)
from sorter import sort
from db_queries import get_all_contacts_from_db, get_all_notes


def main():
    """Main function which calls all functions"""
    commands_list = [
        "jarvis add contact\n",
        "jarvis show contacts\n",
        "jarvis find contact {name}\n",
        "jarvis change contact {name}\n",
        "jarvis delete contact {name}\n",
        "jarvis add phone {name}\n",
        "jarvis get birthdays {days_to}\n",
        "jarvis add note\n",
        "jarvis show notes\n",
        "jarvis find note {id/text/tag}\n",
        "jarvis change note {id}\n",
        "jarvis delete note {id}\n",
        "jarvis add tags {id}\n",
        "jarvis sort folder {path_to_folder}\n",
    ]
    user_commands = {
        "add_contact": add_contact,
        "change_contact": change_contact,
        "del_contact": del_contact,
        "find_contact": find_contact,
        "get_birthdays": get_birthdays,
        "show_all": get_all_contacts_from_db,
        "add_note": add_note,
        "show_notes": get_all_notes,
        "change_note": change_note,
        "delete_note": delete_note,
        "find_note_by_name": find_note_by_name,
        "add_tags": add_tags,
        "sort_folder": sort,
    }
    inp = input("command: ")
    if inp == "help":
        print(
            f'Hello my name is "Jarvis" i am your virtual assistant.\n'
            f'I support these commands:\n  {"  ".join(commands_list)}'
        )
    elif inp in user_commands:
        print(user_commands[inp]())
    else:
        print(f"I do not support this command {inp}")


if __name__ == "__main__":
    main()
