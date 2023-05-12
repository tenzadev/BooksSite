from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import BookForm, TGUserForm
from .models import TGUser
from main.models import Product, Category, Comment
from main.forms import ProductForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


def index(request, cat_slug=None):
    q = request.GET.get('q')
    cats = Category.objects.all()
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=cat)
    elif q:
        products = Product.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {"products": products, "cats": cats})

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        # body = request.POST.get('body')
        # print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': pk}))
    comments = Comment.objects.filter(product=product)
    return render(request, "blog/product_detail.html", {"product": product, "comments": comments})

@login_required(login_url="/users/login/")
def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "main/add_product.html", {"form": form})

@login_required(login_url="/users/login/")
def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("index")
        else:
            print(form.errors)
    return render(request, "blog/create.html", {"form": form})

@login_required(login_url="/users/login/")
def add_user(request):
    form = TGUserForm()
    if request.method == "POST":
        form = TGUserForm(request.POST)
        if form.is_valid():
            # TGUser.objects.create(
            #     tg_id=form.cleaned_data.get('tg_id'),
            #     first_name=form.cleaned_data.get('first_name'),
            #     last_name=form.cleaned_data.get('last_name'),
            #     username=form.cleaned_data.get('username'),
            #     about=form.cleaned_data.get('about'),
            # )
            form.save()
            return redirect('index')
    return render(request, "blog/create_user.html", {"form": form})

@login_required(login_url="/users/login/")
def update_user(request, pk):
    user = TGUser.objects.get(id=pk)
    form = TGUserForm(instance=user)
    if request.method == "POST":
        form = TGUserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "blog/update_user.html", {"form": form})


@login_required
def delete_user(request, pk):
    user = TGUser.objects.get(id=pk)
    user.delete()
    return redirect('index')
