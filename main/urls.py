from django.conf.urls import url
from main.views import *

app_name = 'main'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = 'home'),
]