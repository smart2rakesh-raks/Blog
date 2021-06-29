from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string

from product.forms import productform
from .forms import SignUpForm, loginForm, Postform
from django.contrib import messages
from .models import Post
from product.models import product


# Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def product_view(request):
    if request.user.is_authenticated:
        products = Post.objects.all()
        return render(request, 'product.html', {'posts': products,})
    else:
        return HttpResponseRedirect('/login/')


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        full_name = request.user.get_full_name()
        return render(request, 'dashboard.html', {'posts': posts, 'full_name':full_name})
    else:
        return HttpResponseRedirect('/login/')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Succesfully Signed up")
            form.save()
    else:
        form = SignUpForm
    return render(request, 'signup.html', {'form': form})


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = loginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Postform(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
                pst = Post(text=text, )
                pst.save()
                form = Postform()
                messages.success(request, "Post added successfully")
                return HttpResponseRedirect('/dashboard/')
        else:
            form = Postform()
        return render(request, 'addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            p = Post.objects.get(pk=id)
            form = Postform(request.POST, instance=p)
            if form.is_valid():
                form.save()
                messages.success(request, "Post Updated successfully")
                return HttpResponseRedirect('/dashboard/')
        else:
            p = Post.objects.get(pk=id)
            form = Postform(instance=p)
        return render(request, 'update.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')


def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            p = Post.objects.get(pk=id)
            p.delete()
            messages.success(request, "Post Deleted successfully")
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = productform(request.POST)
            if form.is_valid():
                text = form.cleaned_data['name']
                text = form.cleaned_data['weight']
                text = form.cleaned_data['price']
                pst = product(name=text, weight= text, price=text, )
                pst.save()
                form = productform()
                messages.success(request, "product added successfully")
                return HttpResponseRedirect('/product/')
        else:

            form = productform()
        return render(request, 'add_product.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')