from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# This is just the default page that shows the team description
def indexPageView(request):
    return render(request, 'pages/index.html')

# simple contact page that just renders the html when the route is called
def contactPageView(request):
    return render(request, 'pages/contact.html')

# this page hasn't yet been implemented
# def loginPageView(request) :
#     return render(request, 'pages/login.html')

# this page is referenced in the flashcard.html page and it just returns different student objects based the filters entered
def filterFlashcards(request):
    section = request.POST["section"]
    group = request.POST["group"]
    # radio button needs a default if nothing is passed
    try:
        gender = request.POST["gender"]
    except:
        gender = ""

    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    # uses __contains so that if nothing is entered then it doesn't filter down on the field
    data = Student.objects.filter(fName__contains=firstName, lName__contains=lastName, sectionNum__contains=section, groupNum__contains=group, gender__contains=gender)

    context = {
        'our_students' : data
    }
    return render(request, 'pages/flashcard.html', context)

# default path for flashcard.html that displays all the students
def flashcardPageView(request):
    data = Student.objects.all()
    context = {
        'our_students' : data
    }
    return render(request, 'pages/flashcard.html', context)

# displays all the student objects and has an edit button on the card itself
def libraryPageView(request):
    data = Student.objects.all()
    context = {
        'our_students' : data
    }
    return render(request, 'pages/library.html', context)

# adds a student object and after submission redirects to the library page
def addStudent(request):
# instantiate the student
    thisStudent = Student()
    # add attributes according to the form
    thisStudent.fName = request.POST['firstName']
    thisStudent.lName = request.POST['lastName']
    thisStudent.funfact = request.POST['funfact']
    thisStudent.sectionNum = request.POST['Section']
    thisStudent.groupNum = request.POST['groupNum']
    thisStudent.gender = request.POST['gender']
    thisStudent.photo = request.FILES['photo']
    thisStudent.feedback = request.POST['feedback']

    # print (thisStudent)
    thisStudent.save()

    return libraryPageView(request)

# Gets the data for an individual student object so their data can be edited
def studInfoPageView(request, stud_id):
    data = Student.objects.filter(id = stud_id)
    if len(data) > 1:
        data = ['There was more than one student with this id']

    context = {
        'student' : data[0]
    }
    return render (request, 'pages/studInfo.html', context)

# This is the route that is called when we need to edit a student's information
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
    updatedStud.feedback = request.POST['feedback']
    if len(request.FILES) != 0:
        # if a new file is being appended then delete the old one before creating a new object
        updatedStud.photo.delete()
        updatedStud.photo = request.FILES['photo']
        
    updatedStud.save()
    return libraryPageView(request)

# This is where we can delete students from our database
def delStud(request):
    data = Student.objects.filter(id = request.POST['id'])
    if len(data) > 1:
        return render(request, 'pages/studInfo.html', context = 'That id has more than one student')
    
    deletedStudent = data[0]

    # delete their stored photo before deleting the student found
    deletedStudent.photo.delete()
    deletedStudent.delete()

    return libraryPageView(request)