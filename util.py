import datetime


def clean_and_transform(person):
    contact = {}
    contact['first_name'] = person.get('fields').get('firstName').strip()
    contact['last_name'] = person.get('fields').get('lastName').strip()
    contact['birthdate'] = datetime.datetime.strptime(person.get(
        'fields').get('dateOfBirth'), "%d-%m-%Y").strftime("%Y-%m-%d")
    contact['email'] = person.get('fields').get('email')

    custom_properties = {}
    custom_properties['airtable_id'] = person.get('id')
    custom_properties['lifetime_value'] = float(
        person.get('fields').get('lifetime_value')[1:])

    contact['custom_properties'] = custom_properties

    return contact
