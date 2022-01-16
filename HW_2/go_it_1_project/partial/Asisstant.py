from os import terminal_size
from re import S, T
from partial.AdressBook import *
from partial.NoteBook import *
from abc import ABC, abstractmethod



class Asisstant:
    def __init__(self) -> None:
        self.address_book = AddressBook()
        self.address_book.load_data()
        self.note_book = NoteBook()
        self.note_book.load_data()

    def __get_phone(self, name: str) -> str:
        phone = input("Phone is key value, please write phones: ")
        phones_list = phone.split(",") if phone is not None else []
        while self.address_book[name].get_phones() != phones_list:
            phones_list = phone.split(",") if phone is not None else []
            for item in phones_list:
                self.address_book[name].add_phone(item)
            self.address_book[name].delete_phone([])
            if self.address_book[name].get_phones() != phones_list:
                self.address_book[name].phones.clear()
                phone = input("Phone is key value, please write phones: ")
        self.address_book.save_data()
        return f"Successfully set phone {phone}"

    def __get_birthday(self, name: str) -> str:
        birthday = input(
            '"OPTIONAL" You can skip this info, just press enter\nWrite birthday: '
        )
        if len(birthday) == 0:
            self.address_book[name].birthday.value = None
        else:
            while str(self.address_book[name].birthday.value) != birthday:
                self.address_book[name].add_birthday(birthday)
                if str(self.address_book[name].birthday.value) != birthday:
                    birthday = input(
                        '"OPTIONAL" You can skip this info, just press enter\nWrite birthday: '
                    )
        self.address_book.save_data()
        return f"Successfully set birthday {birthday}"

    def __get_email(self, name: str) -> str:
        email = input(
            '"OPTIONAL" You can skip this info, just press enter\nWrite email: '
        )
        if len(email) == 0:
            self.address_book[name].email.value = None
        else:
            while str(self.address_book[name].email.value) != email:
                self.address_book[name].add_email(email)
                if str(self.address_book[name].email.value) != email:
                    email = input(
                        '"OPTIONAL" You can skip this info, just press enter\nWrite email: '
                    )
        self.address_book.save_data()
        return f"Successfully set email {email}"

    def __get_address(self, name: str) -> str:
        address = input(
            '"OPTIONAL" You can skip this info, just press enter\nWrite address: '
        ).capitalize()
        if len(address) == 0:
            self.address_book[name].address.value = None
        else:
            while str(self.address_book[name].address.value) != address:
                self.address_book[name].add_address(address)
                if str(self.address_book[name].address.value) != address:
                    address = input(
                        '"OPTIONAL" You can skip this info, just press enter\nWrite address: '
                    )
        self.address_book.save_data()
        return f"Successfully set address {address}"

    def add_contact(self) -> str:
        name = input("Name is key value, please write name: ").capitalize()
        while len(name) < 4:
            name = input(
                '"Error" name length must be at least 4, please write name: '
            ).capitalize()
        new_contact = Record(
            name=name, phones=[], birthday=None, email=None, address=None
        )
        self.address_book.add_record(new_contact)
        self.address_book.save_data()
        Asisstant().__get_phone(name)
        Asisstant().__get_birthday(name)
        Asisstant().__get_email(name)
        Asisstant().__get_address(name)
        print(f"[+] Successfully added contact {name} to contact book")

    def __change_name(self, name: str) -> str:
        new_name = input("Write new name: ").capitalize()
        while len(new_name) < 4:
            new_name = input(
                '"Error" name length must be at least 4, please write name: '
            ).capitalize()
        old_record = self.address_book.data[name]
        new_record = Record(
            name=new_name,
            phones=old_record.get_phones(),
            birthday=str(old_record.birthday.value),
            email=old_record.email.value,
            address=old_record.address.value,
        )
        self.address_book.add_record(new_record)
        self.address_book.delete_record(name)
        self.address_book.save_data()
        return f"Successfully changed name for contact {name}"

    def __change_phone(self, name: str) -> str:
        old_phone = input("Write old phone: ")
        while old_phone not in self.address_book[name].get_phones():
            old_phone = input(
                f'I do not have such phone: "{old_phone}", write old phone: '
            )
        self.address_book[name].delete_phone(old_phone)
        new_phone = input("Write new phone: ")
        self.address_book[name].add_phone(new_phone)
        while new_phone not in self.address_book[name].get_phones():
            new_phone = input("Write new phone: ")
            self.address_book[name].add_phone(new_phone)
            self.address_book[name].delete_phone([])
        self.address_book.save_data()
        return f"Successfully changed phone for contact {name}"

    def __change_birthday(self, name: str) -> str:
        new_birthday = input("Write new birthday: ")
        while str(self.address_book[name].birthday.value) != new_birthday:
            self.address_book[name].add_birthday(new_birthday)
            if str(self.address_book[name].birthday.value) != new_birthday:
                new_birthday = input("Write new birthday: ")
        self.address_book.save_data()
        return f"Successfully changed birthday for contact {name}"

    def __change_email(self, name: str) -> str:
        new_email = input("Write new email: ")
        while str(self.address_book[name].email.value) != new_email:
            self.address_book[name].add_email(new_email)
            if str(self.address_book[name].email.value) != new_email:
                new_email = input("Write new email: ")
        self.address_book.save_data()
        return f"Successfully changed email for contact {name}"

    def __change_address(self, name: str) -> str:
        new_address = input("Write new address: ").capitalize()
        while str(self.address_book[name].address.value) != new_address:
            self.address_book[name].add_address(new_address)
            if str(self.address_book[name].address.value) != new_address:
                new_address = input("Write new address: ").capitalize()
        self.address_book.save_data()
        return f"Successfully changed address for contact {name}"

    def change_contact(self, name: str) -> None:

        if name not in self.address_book.keys():
            print(f"I do not have {name} contact in my book")
            name = input("Write contact name: ").capitalize()
        user_commands = {
            "phone": Asisstant().__change_phone,
            "name": Asisstant().__change_name,
            "birthday": Asisstant().__change_birthday,
            "email": Asisstant().__change_email,
            "address": Asisstant().__change_address,
        }
        what_change = input("What you want to change?\n")
        while what_change not in user_commands.keys():
            print("I can change only phone, name, birthday, email, address")
            what_change = input("What you want to change?\n")
        print(user_commands[what_change](name))
        print("Successfully saved new value in data")

    def del_contact(self, name: str) -> None:

        if name not in self.address_book.keys():
            print(f"I do not have {name} contact in my book")
            name = input("Write contact name: ").capitalize()
        approve = input("Are you sure? [y/n]").lower()
        if approve in ("y", "yes", "ok"):
            self.address_book.delete_record(name)
            
            print(f"[-] Successfully deleted contact {name} from contact book")

    def find_contact(self, name: str) -> None:

        result = self.address_book.find_record(name)
        print(result)

    def get_birthdays(self, days: int) -> list:
        while days.isdigit() is False:
            days = input(
                '"Error please enter digits"\nFor how many days do you want to know the birthdays?\n'
            )
        days = int(days)
        birthday_list = self.address_book.birthday_in_days(days)
        for info in birthday_list:
            print(info)

    def __get_text_note(self) -> str:
        text = ""
        while True:
            row = input()
            if row:
                text += row + "\n"
            else:
                break
        return text

    def add_note(self) -> None:
        print("Write down your note:")
        text = self.__get_text_note()

        if text == "":
            return
        text_tags = input("OPTIONAL, write tags to this note: ")
        if text_tags != "":
            tags = text_tags.split(",")
            tags = [tag.strip() for tag in tags]
            self.note_book.add_note(text, tags)
            self.note_book.save_data()
        else:
            self.note_book.add_note(text, [])
            self.note_book.save_data()

    def find_note(self, value: str) -> None:
        notes = self.note_book.find_note(value)
        for note in notes:
            print(note)
            
    @abstractmethod
    def show_notes(self,) -> None:
        if len(self.note_book.data) == 0:
            print("You don't have notes yet.")
            return
        for note in self.note_book.data:
            print(note)

    def change_note(self, id: str) -> None:
        print("Write down your new note: ")
        text = self.__get_text_note()
        self.note_book.change_note(id, text)
        self.note_book.save_data()

    def delete_note(self, id: str) -> None:
        self.note_book.del_note(id)
        self.note_book.save_data()

    def add_tags(self, id: str) -> str:
        text_tags = input("Write tags to this note: ")
        tags = text_tags.split(",")
        tags = [tag.strip() for tag in tags]
        self.note_book.add_note_tags(id, tags)
        self.note_book.save_data()

    def add_phone(self, name:str) -> None:
        name = name.capitalize()
        if name not in self.address_book.keys():
            print(f"I do not have {name} contact in my book")
            name = input("Write contact name: ").capitalize()
        phone = input('Phone: ')
        self.address_book[name].add_phone(phone)
        self.address_book.save_data()
        

class ShowCommands(ABC):
    @abstractmethod
    def show_commands(self):
        pass

    @abstractmethod
    def show_notes(self):
        pass


class Commands(ShowCommands, Asisstant):
    
    def show_commands(self):
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
        return f'Hello my name is "Jarvis" i am your virtual assistant.\nI support these commands:\n  {"  ".join(commands_list)}'

    def show_notes(self,) -> None:
        if len(self.note_book.data) == 0:
            print("You don't have notes yet.")
            return
        for note in self.note_book.data:
            print(note)
    