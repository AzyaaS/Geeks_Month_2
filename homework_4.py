class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            contact = Contact(name, phone_number)
            cls.all_contacts.append(contact)
        else:
            raise ValueError('Ошибка номера телефона')

print(ContactList.all_contacts)
ContactList.add_contact('Rayimbek', '0500230178')
ContactList.add_contact('Aziret', '0500848654')

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("John Doe", "5551234")