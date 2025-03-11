from django.urls import path

from web.views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("notes/add/", note_add_view, name="note_add"),
    path("notes/edit/<int:note_id>/", note_edit, name="note_edit"),
    path("notes/view/<int:note_id>/", note_view_view, name="note_view"),

]
