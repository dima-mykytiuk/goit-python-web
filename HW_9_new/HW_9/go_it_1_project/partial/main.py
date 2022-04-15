from Asisstant import Asisstant
from Sorter import Sorter
from HW_9_new.HW_9.sql_changes import get_all_contacts_from_db, get_all_notes

def main():
    jarvis = Asisstant()
    commands_list = [
        "jarvis add contact\n",
        "jarvis show contacts\n",
        "jarvis find contact {name}\n",
        "jarvis change contact {name}\n",
        "jarvis delete contact {name}\n",
        "jarvis add phone {name}"
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
        "add_contact": jarvis.add_contact,
        "change_contact": jarvis.change_contact,
        "del_contact": jarvis.del_contact,
        "find_contact": jarvis.find_contact,
        "get_birthdays": jarvis.get_birthdays,
        "show_all": get_all_contacts_from_db,
        "add_note": jarvis.add_note,
        "show_notes": get_all_notes,
        "change_note": jarvis.change_note,
        "delete_note": jarvis.delete_note,
        "find_note_by_name": jarvis.find_note_by_name,
        "add_tags": jarvis.add_tags,
        "sort_folder": Sorter().sort,
    }
    inp = input('command: ')
    if inp == 'help':
        f'Hello my name is "Jarvis" i am your virtual assistant.\nI support these commands:\n  {"  ".join(commands_list)}'
    elif inp in user_commands.keys():
        user_commands[inp]()
    else:
        print(f"I do not support this command {inp}")
    
    
if __name__ == "__main__":
    main()
