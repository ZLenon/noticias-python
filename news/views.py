from django.shortcuts import render, redirect
from news.models import News
from news.form import FormCategories


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
