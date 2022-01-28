from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from core.models import CustomUser as User
from sawo import createTemplate, getContext, verifyToken
import json
import os
import requests


load = ''
loaded = 0


def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded=0
    else:
        loaded+=1

createTemplate("templates/partials")

def index(request):
    return render(request,"index.html")

def login(request):
    setLoaded()
    setPayload(load if loaded<2 else '')
    # print(config('api_key'))
    configuration = {
                "auth_key": os.environ.get("SELLER_API_KEY"),
                "identifier": "email",
                "to": "seller/receive"
    }
    context = {
                "sawo": configuration,
                "load": load,
                "title": "Home"
            }

    return render(request,"login.html", context)

def receive(request):
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        setLoaded(True)
        setPayload(payload)

        test_payload = {}
        test_payload['user_id'] = payload.get('user_id')
        test_payload['verification_token'] = payload.get('verification_token')
        print(test_payload)
        verifyURL = 'https://api.sawolabs.com/api/v1/userverify/'
        verify = requests.post(verifyURL, json=test_payload)
        status = int(verify.status_code)
        if status == 200:
            print('party')
            email = payload.get('identifier')
            duplicate_users = User.objects.filter(email=email)
            print(duplicate_users, 'ho raha hai')
            if not duplicate_users.exists():
                print('maaro mujhe')
                user_id = payload.get('user_id')
                is_buyer = False
                is_seller = True
                seller_name = payload.get('customFieldInputValues').get('Seller Name')
                print(seller_name, type(seller_name))
                User.objects.create_user(
                                            user_id,
                                            email=email,
                                            is_buyer=is_buyer,
                                            is_seller=is_seller,
                                            seller_name=str(seller_name))

        response_data = {"status": status}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
