from django.urls import path
from .views import indexPageView, contactPageView, flashcardPageView, loginPageView, libraryPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("contact", contactPageView, name="contact"),
    path("flashcards", flashcardPageView, name="flashcard"),
    path('login', loginPageView, name='login'),
    path('library', libraryPageView, name="library"),
]