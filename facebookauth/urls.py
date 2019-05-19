from django.conf.urls import url
from facebookauth.views import *

app_name = 'facebookauth'

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name ='login'),
    url(r'^logout/', LogoutView.as_view(), name = 'logout'),
]