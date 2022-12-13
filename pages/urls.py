from django.urls import path
from .views import * # indexPageView, contactPageView, flashcardPageView, loginPageView, libraryPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("contact", contactPageView, name="contact"),
    path("flashcards", flashcardPageView, name="flashcard"),
    path('login', loginPageView, name='login'),
    path('library', libraryPageView, name="library"),
    path('addStudent', addStudent, name="addStudent"),
    path('editStudent/<int:stud_id>/',  studInfoPageView, name='studInfoPageView'),
    path('editStudent', editStudent, name='editStudent'),
    path('delStud', delStud, name='delStud'),
    path('filter', filterFlashcards, name='filter'),
]