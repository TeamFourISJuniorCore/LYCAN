from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Hello Universe!')

# Create your views here.
