import os
from api import ApiRequest

from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ["API_URL"]
TOKEN = os.environ["TOKEN"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


api_request = ApiRequest(API_URL, TOKEN, USERNAME, PASSWORD)
api_request.post_contacts()
