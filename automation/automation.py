import shutil

from faker import Faker

fake = Faker('en_US')

potential_contacts = ""



for _ in range(100):
    potential_contacts += fake.paragraph()
    potential_contacts += fake.email()
    potential_contacts += fake.address()
    potential_contacts += fake.phone_number()
    potential_contacts += fake.word()

with open('automation/potential-contacts.txt', 'w+') as file:
    file.write(potential_contacts)



shutil.copy('contacts.txt', 'contacts.txt.bak')