from django.views import generic, View
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from .forms import CreateUserForm,content
from django.contrib.auth import authenticate,login,logout

    
class PostList(generic.ListView):
    def get(self, request, *args, **kwargs):
     queryset = Post.objects.filter(Status=1).order_by('-Created_On')
     context = {"post_list":queryset}
     return render(request,'index.html',context)


class PostDetail(View):
    def get(self, request, *args, **kwargs):
       details = Post.objects.latest('pk')
       context = {'Details': details}
       return render(request, 'post_detail.html', context)

def gc_register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was Created for'+  user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html',context)

def gc_login(request):
    if request.method=="POST":
       username =  request.POST.get('username')

       password=  request.POST.get('password')
       user = authenticate(request,username=username,password=password)
       if user is  None:
           login(request,user)
           return redirect('/')
       else:
           messages.info(request,'Username or Password is Incorrect')

    return render(request,'login.html')

def gc_logout(request):
    logout(request)
    return redirect('/')

def gc_content(request):
    form = content
    if request.method == 'POST':
        form = content(request.POST)
        if form.is_valid():
            form.save()
            def get(self, request, *args, **kwargs):
                        queryset = Post.objects.filter(Status=1).order_by('-Created_On')
                        
                        context = {"post_list": queryset}
                        return render(request,"index.html", context)

    context = {'form': form}
    return render(request, 'content.html', context)




