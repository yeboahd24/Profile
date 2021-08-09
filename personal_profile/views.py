from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

# Blog page
def blog(request):
    return render(request, 'blog-dark.html')


# Index
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        send_mail('Contact', message, email, ['yeboahd24@gmail.com'])
        return redirect('index')
    return render(request, 'index-dark.html')


# Single
def single(request):
    return render(request, 'single-work.html')
