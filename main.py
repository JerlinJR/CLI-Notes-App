import requests
import json
import sys
from jsonpath_ng import jsonpath, parse

baseUrl = "https://apitest.jerlin.space/api"


def login(username,password):
    
    url = "https://apitest.jerlin.space/api/auth/login"
    payload={ 
             'username': username,
             'password': password }
    headers = {
        
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(response.text)
    # jsonpath_expr = parse('token')
    # result = jsonpath_expr.find(response)[4].value
    # print(result)
    
def signup(username,email,password):
    
    url = "https://apitest.jerlin.space/api/auth/signup"
    payload={
        'username': username,
        'email': email,
        'password': password
        }
    
    headers = {
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    
def getAllNotes(uid,token):

    url = "https://apitest.jerlin.space/api/folder/get_all_notes"

    payload={
        'id': uid
        }
    
    headers = {
    'Authorization': 'Bearer'+ token,
    # TODO: Check wheather we need SessionId
    # 'Cookie': 'PHPSESSID=h1icsb10tqm5cigff8pce8'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

def getNote(noteId,token):
    
    url = "https://apitest.jerlin.space/api/notes/get"

    payload={
        'id': noteId
             }

    headers = {
    'Authorization': 'Bearer'+ token,
    # TODO: SessionCheck
    # 'Cookie': 'PHPSESSID=h1icsb10tqm5cigffce8'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

def refreshAcessToken(rtoken,):
    
    url = "https://apitest.jerlin.space/api/auth/refresh?refresh_token="+rtoken

    headers = {
        # TODO: ID check
    'Cookie': 'PHPSESSID=h1icsb10tqmpce8'
    }

    response = requests.request("POST", url, headers=headers,)
    print(response.text)





