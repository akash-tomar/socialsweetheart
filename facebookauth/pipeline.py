import requests
import json
from facebookauth.models import AccessToken

def getLongLiveToken(response):
    payload = {
        "grant_type": "fb_exchange_token",
        "client_id": "352111075652896",
        "client_secret": "4f41fbed5c930dbb050c50fa85e08af2",
        "fb_exchange_token": response["access_token"]
    }
    r = requests.get('https://graph.facebook.com/oauth/access_token', params = payload)
    JSON = json.loads(r.text)
    return JSON["access_token"]

def load_user(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        # import pdb; pdb.set_trace()
        social_user = user.social_auth.get(provider='facebook')
        isPresent = False
        try:
            AccessToken.objects.get(id = social_user.id)
            isPresent = True
        except:
            pass
        if not isPresent:
            long_live_token = getLongLiveToken(response)
            access_token = AccessToken(id = social_user.id, access_token = long_live_token, social_auth = social_user)
            access_token.save()