from django.shortcuts import render

# Create your views here.
from index.models import news, page1, about, service


def index(request):
    return render(request, 'index/index.html', {})

def get_news(request):
    news_res = news.objects.all()
    dic = {"news": news_res}
    return render(request, 'web/new-list.html', dic)


def get_index(request):
    page1_res = page1.objects.all()
    dic = {"page_index": page1_res}
    return render(request, 'web/index.html', dic)



def get_about(request):
    about_res = about.objects.all()
    dic = {"page_index": about_res}
    return render(request, 'web/about_us.html', dic)


def get_service(request):
    service_res = service.objects.all()
    dic = {"page_index": service_res}
    return render(request, 'web/service.html', dic)



def get_solve(request):
    return render(request, 'web/solve.html', {})

def get_pmcon(request):
    return render(request, 'web/pm_con.html', {})
