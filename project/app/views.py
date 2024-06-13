from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Book,User
from .forms import BookForm,SignUpForm,LogInForm
import time

#Login


def login_page(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email,password=password).first()
            if user:
                return redirect('book_list')
            else:
                return render(request, 'login_page.html', {'form': form, 'error_message': 'Invalid Email or Password.'})
    else:
        form = LogInForm()
    return render(request, 'login_page.html', {'form': form})

#Signup


def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(email=email).exists():
                return render(request, 'signup_page.html', {'form': form, 'error_message': 'Email is already taken.'})
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save()
                return redirect('login_page')
    else:
        form = SignUpForm()
    return render(request, 'signup_page.html', {'form': form})

#create

def book_create(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            time.sleep(1)
            return redirect('book_list')
    else:
            form = BookForm()
    return render(request,'book_form.html',{'form':form})
    
#read

def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'books':books})

def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request,'book_detail.html',{'book':book})

#Update

def book_update(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            time.sleep(1)
            return redirect('book_list')
    else:
            form=BookForm()
    return render(request,'book_form.html',{'form':form})    

#Delete

def book_delete(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method=='POST':
        book.delete()
        time.sleep(1)
        return redirect('book_list')
    return render(request,'book_confirm_delete.html',{'book':book}) 