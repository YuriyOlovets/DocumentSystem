import json
import requests

from app import cache
from app.documents.sql import user_detail

def make_request(hash):
    headers = {'Content-Type':'application/json', 'secret_key':'yOJjE9L9OnLInXH1rrMBdZQdpzqUKnmM'}
    data =  {
        'operation':'query',
        'elementType':'Contacts',
        'query':user_detail(hash),
        'new_query':user_detail(hash),
        'test_fake': True
        }

    url = "https://agent-api.acggroupcom.com/sync/webservice/v1"
    response = requests.post(url, headers=headers, data=json.dumps(data))

    try:
        result_dict = response.json()[0]
    except:
        return ('User does not exist', 204)

    cache.set(hash, result_dict, 900)
    return result_dict

