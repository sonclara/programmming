from django.conf.urls import url
from django.contrib.auth.views import login
from accounts import views, forms



urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login/$', login, kwargs={
        'authentication_form': LoginForm,
        }),
    url(r'^profile/$', views.profile),
]