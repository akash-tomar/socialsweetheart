from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.views import View
import requests
import json
from django.urls import reverse

def getName(userid, payload):
    r = requests.get('https://graph.facebook.com/v3.3/' + userid , params = payload)
    # import pdb; pdb.set_trace()
    return json.loads(r.text)['name']

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('facebookauth:login'))
            
        fb_user = request.user.social_auth.get(provider='facebook')
        name = getName(fb_user.uid, {"access_token": fb_user.access_token.access_token})
        return render(request, 'home.html', {"name": name, "uid": fb_user.uid, 'url': reverse})