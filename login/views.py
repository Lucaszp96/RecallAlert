from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
# from django.contrib.auth.models import User
from django.db.models import Q

from .forms import UserRegisterForm
from .models import Category, Message as C_Message, Product


def index(request):
    context = {}
    for cat in Category.objects.all():
        print(cat.id, cat.title)
    products = Product.objects.all()[:5]
    context['products'] = products
    print(products)
    return render(request, "login/index.html", context)


def about(request):
    context = {}
    return render(request, "login/about.html", context)


def category(request, cid):
    context = {}
    category = get_object_or_404(Category, id=cid)
    products = category.product_set.all()
    context['current'] = str(int(cid) - 1)
    context['products'] = products

    return render(request, "login/category.html", context)


def product(request, id):
    context = {}
    product = get_object_or_404(Product, id=id)
    context['product'] = product
    print(product)
    return render(request, "login/product.html", context)


# @login_required
# def account(request):
#     context = {}
#     return render(request, "login/index.html", context)


# Register
def register(request):
    if request.user.is_authenticated:
        return redirect("index")

    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            messages.success(
                request,
                f"{username} account registered successfully，please login！")
            return redirect("login")
        else:
            messages.error(request,
                           "Register failed, username or password error！")
    return render(request, "login/register.html", {'form': form})


def search(request):
    context = {}
    if request.method == "POST":
        keyword = request.POST.get('keyword', None)
        print(keyword)
        if keyword is None:
            messages.error(request, "No keyword")
            return redirect('index')
        cond = Q(product_name__icontains=keyword) | Q(sn__icontains=keyword)
        products = Product.objects.filter(cond)
        print(products)
        context['products'] = products
        context['keyword'] = keyword
        return render(request, "login/search.html", context)
    return redirect('index')


def contact(request):
    context = {}
    if request.method == "POST":
        pname = request.POST.get("pname")
        psn = request.POST.get("psn")
        pdetail = request.POST.get("pdetail")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        C_Message.objects.create(name=name,
                                 email=email,
                                 phone=phone,
                                 product_name=pname,
                                 product_sn=psn,
                                 product_detail=pdetail)
        messages.success(request,
                         f"{name}'s message was submitted successfully！")

    return render(request, "login/contact.html", context)
