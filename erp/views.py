from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse

# Create your views here.


def api(request):
    print(reverse('erp:api'))
    return HttpResponse('erp:接口自动化平台')
