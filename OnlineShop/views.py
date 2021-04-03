from django.shortcuts import render, redirect
from .models import *


def main_page(request):
    # get array of elemetns all elements
    products = Product.objects.all()
    # get only one element
    # articles = Article.objects.get(pk=1)
    d = {
        "products": products
    }

    return render(request, "OnlineShop/main_page.html", context=d)


def detail_page(request, id):
    product = Product.objects.get(pk=id)
    d = {
        "product": product,
    }
    return render(request, "OnlineShop/detail_page.html", context=d)


def add_page(request):
    return render(request, "OnlineShop/add_page.html")


def add_page_action(request):
    name = request.POST["name"]
    price = request.POST["price"]
    image = request.POST["image"]
    description = request.POST["description"]
    article = Product(name=name, price=price, image=image, description=description)
    article.save()
    return redirect("main_page")