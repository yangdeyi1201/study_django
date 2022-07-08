from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views import View
from django.urls import reverse
import json

# Create your views here.


def student_detail(request, sid):
    """根据学生学号返回页面响应"""
    print(reverse('students:s_detail', kwargs={'sid': 18}))  # 反向解析路由
    print(f'@:{type(sid)}')  # 只有int路径转换器才会进行转换，其它包含正则都不会转换
    return HttpResponse(f'学号为{sid}的学生详情')


def student_list(request, month, year):
    """路径参数查询指定年月报名的学生列表"""
    print(reverse('students:s_year_month', kwargs={'year': '2050', 'month': '11'}))  # 反向解析路由
    return HttpResponse(f'{year}年{month}月报名的学生列表')


def student_list_api(request):
    """json格式返回学生列表"""
    print(reverse('students:students.json'))  # 反向解析路由
    students = [{'name': 'yangdeyi', 'sex': 'male', 'age': 18},
                {'name': 'hejiuping', 'sex': 'female', 'age': 19},
                {'name': 'yangqingliang', 'sex': 'male', 'age': 20}]
    return JsonResponse(data=students, safe=False)  # 非字典转json, 必须设置safe=False


def search(request):
    """queryString查询"""
    return HttpResponse('-'.join(request.GET.values()))


def login(request):
    if request.method == 'GET':
        return render(request=request, template_name='students/login.html')
    elif request.method == 'POST':
        username, password = None, None
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            username, password = data.get('username'), data.get('password')
        elif request.content_type in ('application/x-www-form-urlencoded', 'multipart/form-data'):
            username, password = request.POST.get('username'), request.POST.get('password')
        return HttpResponse('登录成功') if username == 'admin' and password == '111111' else HttpResponse('用户名密码错误!')


class Login(View):

    @staticmethod
    def get(request):
        return render(request, 'students/login.html')

    @staticmethod
    def post(request):
        username, password = None, None
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            username, password = data.get('username'), data.get('password')
        elif request.content_type in ('application/x-www-form-urlencoded', 'multipart/form-data'):
            username, password = request.POST.get('username'), request.POST.get('password')
        return HttpResponse('登录成功') if username == 'admin' and password == '111111' else HttpResponse('用户名密码错误!')

# 非post方法发送的x-www-form-urlencoded表单, 可通过下面方式转成字典形式拿取表单参数
# dict([kv.split('=') for kv in re.search(r"b'(.*?)'", str(request.body)).group(1).split('&')])
