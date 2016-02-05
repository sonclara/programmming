from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views
from accounts.forms import LoginForm



urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login/$', login, kwargs={
        'authentication_form': LoginForm,
        }),
    url(r'^profile/$', views.profile),
    url(r'^logout/$', logout, name="auth_logout"),
]