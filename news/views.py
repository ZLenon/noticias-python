from django.shortcuts import render
from news.models import News


def home(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news = News.objects.get(id=id)
    return render(request, "news_details.html", {"news": news})
