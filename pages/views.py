from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def indexPageView(request):
    #uncomment everything between here until the return for printing all things from the table
    data = Student.objects.all()
    context = {
        'our_students' : data
    }
    return render(request, 'pages/index.html', context)

    #uncomment everything below here to print filtered objects from the table
    # data = Student.objects.filter(lName="Heath")

    # if data.count() > 0:
    #     context = {
    #         'our_students' : data
    #     }
    # else :
    #     context = {
    #         'results' : 'sad day:( no results'
    #     }

    # return render(request, 'pages/index.html', context)

def contactPageView(request):
    return render(request, 'pages/contact.html')

def loginPageView(request) :
    return render(request, 'pages/login.html')

def flashcardPageView(request):
    data = Student.objects.all()
    context = {
        'our_students' : data
    }
    return render(request, 'pages/flashcard.html', context)

def libraryPageView(request):
    return render(request, 'pages/library.html')


# # for reference:
# def indexPageView(request):
#     outputHTML = '<html><h1>This is the Home Page!</h1>'
#     outputHTML += '<ul><li><a href="/contact">Contact</a></li>'
#     outputHTML += '<li><a href="/flashcards">Flashcards</a></li>'
#     outputHTML += '<li><a href="/library">Library</a></li>'
#     outputHTML += '<li><a href="/login">login</a></li></ul></html>'
#     return HttpResponse(outputHTML)

# def contactPageView(request):
#     return HttpResponse('<html><h1>This is the Contact Page!</h1><ul><li><a href="/">Home</a></li><li><a href="/flashcards">Flashcards</a></li><li><a href="/library">Library</a></li><li><a href="/login">login</a></li></ul></html>')

# def loginPageView(request) :
#     return HttpResponse('<html><h1>This is the Login Page!</h1><ul><li><a href="/contact">Contact</a></li><li><a href="/flashcards">Flashcards</a></li><li><a href="/library">Library</a></li><li><a href="/">Home</a></li></ul></html>')

# def flashcardPageView(request):
#     return HttpResponse('<html><h1>This is the Flashcard Page!</h1><ul><li><a href="/contact">Contact</a></li><li><a href="/">Home</a></li><li><a href="/library">Library</a></li><li><a href="/login">login</a></li></ul></html>')

# def libraryPageView(request):
#     return HttpResponse('<html><h1>This is the Library Page!</h1><ul><li><a href="/contact">Contact</a></li><li><a href="/flashcards">Flashcards</a></li><li><a href="/">Home</a></li><li><a href="/login">login</a></li></ul></html>')