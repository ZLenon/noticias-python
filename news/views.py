from django.shortcuts import render, redirect
from news.models import News, Categories
from news.form import FormCategories, FormNews


def home(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news = News.objects.get(id=id)
    return render(request, "news_details.html", {"news": news})


def categories_form(request):
    form = FormCategories()
    if request.method == "POST":
        form = FormCategories(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    return render(request, "categories_form.html", {"form": form})


def news_form(request):
    form = FormNews()
    if request.method == "POST":
        form = FormNews(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    return render(
        request,
        "news_form.html",
        {"form": form, "categories": Categories.objects.all()},
    )
