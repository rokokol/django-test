from django.urls import path

from web.views import index_view, registration_view, auth_view

urlpatterns = [
    path("", index_view, name="index"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
]
