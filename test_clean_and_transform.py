from util import clean_and_transform


def test_clean_and_transform():
    data = {
        "id": "rec123456789",
        "fields": {
            "firstName": " James",
            "lastName": "Larry",
            "dateOfBirth": "31-01-1986",
            "email": "jlarry@example.co",
            "lifetime_value": "$125500.00"
        }
    }

    cleaned_and_transformed_data = {
        "first_name": "James",
        "last_name": "Larry",
        "birthdate": "1986-01-31",
        "email": "jlarry@example.co",
        "custom_properties": {
            "airtable_id": "rec123456789",
            "lifetime_value": 125500.0
        }
    }

    assert cleaned_and_transformed_data == clean_and_transform(data)
