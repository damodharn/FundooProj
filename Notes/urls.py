from django.urls import path

from .views import NoteApi


app_name = "notes"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('notes/', NoteApi.as_view()),
]