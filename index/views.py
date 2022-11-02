from django.shortcuts import render

# Create your views here.
from index.models import news, page1, about, service, pm_con


def index(request):
    return render(request, 'index/index.html', {})

def get_news(request):
    if request.GET:
        type= request.GET['type']
        news_res= news.objects.get(type=type)
        dic = {"new": news_res}
        return render(request, 'web/detail.html', dic)

    news_res = news.objects.all()
    dic = {"news": news_res}
    return render(request, 'web/new-list.html', dic)


def get_index(request):
    page1_res = page1.objects.all()
    dic = {"page_index": page1_res}
    return render(request, 'web/index.html', dic)



def get_about(request):
    about_res = about.objects.all()
    dic = {"about": about_res}
    return render(request, 'web/about_us.html', dic)


def get_service(request):
    if request.GET:
        type= request.GET['type']
        service_res= news.objects.get(type=type)
        dic = {"service": service_res}
        return render(request, 'web/service_detail.html', dic)

    service_res = service.objects.all()
    dic = {"services": service_res}
    return render(request, 'web/service.html', dic)



def get_solve(request):
    return render(request, 'web/solve.html', {})

def get_pmcon(request):
    con_res = pm_con.objects.all()
    dic = {"con": con_res}
    return render(request, 'web/pm_con.html', dic)
