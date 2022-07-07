from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse

# Create your views here.


def api(request):
    print(reverse('erp:api'))
    # 准备渲染数据
    title_1, title_2 = 'erp首页面', 'erp副页面'
    content = {'title_1': title_1, 'title_2': title_2}
    # 渲染模板, 返回 html 响应
    return render(request=request, template_name='erp/index.html', context=content)
