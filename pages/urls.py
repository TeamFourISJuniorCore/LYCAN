from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"),
    path("contact", contactPageView, name="contact"),
    path("flashcards", flashcardPageView, name="flashcard"),
    path('library', libraryPageView, name="library"),
    # path('login', loginPageView, name="login"),
    path('addStudent', addStudent, name="addStudent"),
    path('editStudent/<int:stud_id>/',  studInfoPageView, name='studInfoPageView'),
    path('editStudent', editStudent, name='editStudent'),
    path('delStud', delStud, name='delStud'),
    path('filter', filterFlashcards, name='filter'),
]

# description:
    # indexPageView, homepage, basic info
    # contactPageView, sends an email to us if feedback is given
    # flashcardPageView, this is the route that queries the database for all of the students and displays flashcards for each
    # loginPageView, not in use
    # libraryPageView, this also queries the database for all of the students but displays pictures and account informa
    # addStudent, This a route that recieves a form to add a student
    # StudInfoPageView, This displays the student info for the selected student
    # editStudent, This recieves a form that modifies the selected student's credentials
    # delStud, This recieves a form and deletes the student associated with that ID
    # filterFlashcards, this recieves the form from the flashcard page, queries selected rows, and returns the filtered flashcard page