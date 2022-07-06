from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse


# Create your views here.


def student_detail(request, sid):
    """根据学生学号返回页面响应"""
    print(reverse('students:s_detail', kwargs={'sid': 18}))  # 反向解析路由
    print(f'@:{type(sid)}')  # 只有int路径转换器才会进行转换，其它包含正则都不会转换
    return HttpResponse(f'学号为{sid}的学生详情')


def student_list(request, month, year):
    """返回指定年月报名的学生列表"""
    print(reverse('students:s_year_month', kwargs={'year': '2050', 'month': '11'}))  # 反向解析路由
    return HttpResponse(f'{year}年{month}月报名的学生列表')
