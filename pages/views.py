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
    data = Student.objects.all()
    context = {
        'our_students' : data
    }
    return render(request, 'pages/library.html', context)

def addStudent(request):
    # if request.method = POST: Not sure how to implement this line. It's in the text book
    
# add a student here, then redirect to flashcard page
# instantiate the student
    thisStudent = Student()
    # add attributes according to the form
    thisStudent.fName = request.POST['firstName']
    thisStudent.lName = request.POST['lastName']
    thisStudent.funfact = request.POST['funfact']
    thisStudent.sectionNum = request.POST['Section']
    thisStudent.groupNum = request.POST['groupNum']
    thisStudent.gender = request.POST['gender']
    thisStudent.photo = request.POST['photo']
    thisStudent.feedback = request.POST['feedback']
    # thisStudent.fName = request.POST['firstName']
    print (thisStudent)
    thisStudent.save()

    # data = Student.objects.all()
    # context = {
    #     'our_students' : data
    # }
    # return render(request, 'pages/library.html', context)
    return libraryPageView(request)


def studInfoPageView(request, stud_id):

    data = Student.objects.filter(id = stud_id)

    if len(data) > 1:
        data = ['There was more than one student with this id']

    context = {
        'student' : data[0]
    }
    return render (request, 'pages/studInfo.html', context)


def editStudent(request):

    data = Student.objects.filter(id = request.POST['id'])

    if len(data) > 1:
        return render(request, 'pages/studInfo.html', context = 'That id has more than one student')

    updatedStud = data[0]
    updatedStud.fName = request.POST['firstName']
    updatedStud.lName = request.POST['lastName']
    updatedStud.funfact = request.POST['funfact']
    updatedStud.sectionNum = request.POST['Section']
    updatedStud.groupNum = request.POST['groupNum']
    updatedStud.gender = request.POST['gender']
    updatedStud.photo = request.POST['photo']
    updatedStud.feedback = request.POST['feedback']

    updatedStud.save()

    return libraryPageView(request)



def delStud(request):
    data = Student.objects.filter(id = request.POST['id'])
    
    if len(data) > 1:
        return render(request, 'pages/studInfo.html', context = 'That id has more than one student')
    
    deletedStudent = data[0]

    print('We deleted {} {}'.format(deletedStudent.fName, deletedStudent.lName))

    deletedStudent.delete()

    return libraryPageView(request)
    

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