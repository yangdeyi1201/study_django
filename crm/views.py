from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse

# Create your views here.


def api(request):
    print(reverse('crm:api'))
    return HttpResponse('crm:接口自动化平台')
