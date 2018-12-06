from django.shortcuts import render, HttpResponse

# Create your views here


def home(request):
    name = "Seppo"
    email = "seppo@sep.se"

    args = {'name': name, 'email': email}

    return render(request, 'accounts/home.html', args)   
