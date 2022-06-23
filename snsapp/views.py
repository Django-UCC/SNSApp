from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            return render(request, 'signup.html')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})
    return render(request, 'signup.html' ,{})

# Create your views here.
