from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.



def Home(request):
    context={
        "name":"Dakshesh Vashisth"
    }


    return render(request,'home.html',context)


def News(request):
    return render(request, 'news.html')

def Contact(request):
    return render(request, 'contact.html')