from django.urls import path

from web.views import index_view, registration_view, auth_view, logout_view, note_add_view

urlpatterns = [
    path("", index_view, name="index"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("notes/add/", note_add_view, name="note_add"),
]
