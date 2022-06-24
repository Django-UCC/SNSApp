from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from snsapp.models import PostModel

# 会員登録
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            return redirect('list')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})
    return render(request, 'signup.html' ,{})

# ログイン
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html',{'error': 'ユーザーが登録されていません。'})
    return render(request, 'login.html' ,{})

def listfunc(request):
    postsList = PostModel.objects.all()
    return render(request, 'list.html', {'postsList': postsList})
