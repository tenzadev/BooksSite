from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import OrderForm


def main_page(request: HttpRequest):
    # Views Logic
    return HttpResponse("<h1>Hello, Django!</h1><a href='/about/'>About</a> <a href='/contact/'>Contact</a><br><img src='https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1060&t=st=1681303318~exp=1681303918~hmac=e3b8ecbc2ca3908f6a814f429fa55481a62e936baefa543b367de946cfebed9e' alt='Rasm bor edi!'>")

def about_page(request: HttpRequest):
    # print(request.method, request.content_type, request.user, request.path)
    return HttpResponse("<h1 style='text-align: center;'>About Page</h1><a href='/'>Home</a> <a href='/contact/'>Contact</a>")

def contact_page(request: HttpRequest):
    return HttpResponse("<h1>Contact page</h1><a href='/about/'>About</a> <a href='/'>Home</a>")


def add_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "main/add_order.html", {"form": form})
