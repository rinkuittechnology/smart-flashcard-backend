from django.urls import path
from . import views

urlpatterns = [
    path('flashcard', views.add_flashcard, name='add-flashcard'),
    path('get-subject', views.get_flashcards_by_subject, name='get-subject-flashcards'),
]