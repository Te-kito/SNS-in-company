from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required 
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        username2= request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html',{'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2,'',password2)
            return redirect('login')

    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2= request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)

        # ? ユーザーがいる場合
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html',{'error':'ログインに失敗しました'})
    return render(request,'login.html')

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request,'list.html', {'object_list':object_list})
            
def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    loginuser_name = request.user.get_username()
    # ? readtextFieldで分岐する, 
    # ? post.readtextでオブジェクトの中で既読している人のデータを持ってこれる
    # ? request.user.get_username() 今まさに、既読ボタンを押そうとしている人
    if loginuser_name in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + loginuser_name
        post.save()
    return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ['title', 'content', 'author', 'images']
    success_url = reverse_lazy('list')


