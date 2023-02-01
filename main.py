from api import ApiRequest

API_URL = 'https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app'
TOKEN = 'fFz8Z7OpPTSY7gpAFPrWntoMuo07ACjp'
USERNAME = 'datacose'
PASSWORD = '196D1115456D7'


api_request = ApiRequest(API_URL, TOKEN, USERNAME, PASSWORD)
api_request.post_contacts()
