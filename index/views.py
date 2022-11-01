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
def get_index(request):
    return render(request, 'web/index.html', {})



def get_about(request):
    return render(request, 'web/about_us.html', {})

def get_service(request):
    return render(request, 'web/service.html', {})

def get_solve(request):
    return render(request, 'web/solve.html', {})

def get_pmcon(request):
    return render(request, 'web/pm_con.html', {})
