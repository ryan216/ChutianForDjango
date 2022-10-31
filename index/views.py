from django.shortcuts import render

# Create your views here.
from index.models import news


def index(request):
    return render(request, 'index/index.html', {})


def get_news(request):
    dic = {}
    news_res = news.objects.all()
    dic = {"news": news_res}

    return render(request, 'web/new-list.html', dic)
