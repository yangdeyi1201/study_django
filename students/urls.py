"""
============================
Author:杨德义
============================
"""
# 路径转换器匹配范围(由小至大), 默认不写即为str,
# int匹配非负整数, str比slug多匹配中文, path比str多匹配路径分割符 /
# path_converters = ('int', 'slug', 'str', 'path')

# 正则表达式分组命名方式: (?P<分组命名>表达式)
# re_path: 值均以字符串格式传递给视图, 不会进行路径类型转换

from django.urls import path, re_path
from . import views

app_name = 'students'

urlpatterns = [
    path('<int:sid>', views.student_detail, name='s_detail'),
    # 正则匹配 1900-2099 年所有月份
    re_path(r'^(?P<year>19\d?\d|20\d?\d)-(?P<month>[1-9]|0[1-9]|1[0-2])$', views.student_list, name='s_year_month'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('students.json', views.student_list_api, name='students.json')
]
