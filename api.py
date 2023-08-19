import requests
from requests.auth import HTTPBasicAuth
from auth import BearerAuth
from util import clean_and_transform


class ApiRequest():
    """An ApiRequest object definition."""

    def __init__(self, base_url, token, username, password):
        self.base_url = base_url
        self.token = token
        self.username = username
        self.password = password

    def get_people(self):
        response = requests.get(
            self.base_url + '/people/', auth=BearerAuth(self.token))
        return response.status_code, response.json()

    def post_contacts(self):
        status_code, people = self.get_people()
        if status_code == 200:
            for person in people:
                contact = clean_and_transform(person)
                response = requests.post(
                    self.base_url + '/contacts/', json=contact, auth=HTTPBasicAuth(self.username, self.password))
                print('Posting contact', 'response code', response.status_code)
