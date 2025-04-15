from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'library/home.html')


def admin_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if login.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please use a different one.")
            return redirect('home')

        admin = login(
            name=name,
            contact=contact,
            username=username,
            password=password,
        )
        admin.save()
        messages.success(request, "Admin registered successfully! Please login.")
        return redirect('admin_login') 

    return render(request, 'library/admin_signup.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = login.objects.get(username=username)
            if user and user.password == password:
                request.session['id'] = user.id
                request.session['name'] = user.username
                messages.success(request, "Login successful")
                return redirect('book_list')
            else:
                message = "Password Does Not Match"
                return render(request, "library/home.html", {"msg": message})
        except login.DoesNotExist:
            message = "User Does Not Exist. Please Register"
            return render(request, "library/home.html", {"msg": message})
    else:
        return render(request, "library/admin_login.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        Book.objects.create(title=title, author=author, description=description)
        return redirect('book_list')

    return render(request, 'library/add_book.html')

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return redirect('book_list')

    return render(request, 'library/edit_book.html', {'book': book})


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')


