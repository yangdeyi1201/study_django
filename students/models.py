from django.db import models

# Create your models here.


class Student(models.Model):
    sid = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name='姓名', help_text='姓名', max_length=20, blank=False, unique=False, null=False)
    age = models.SmallIntegerField(verbose_name='年龄', help_text='年龄', blank=True, unique=False, null=True)
    sex = models.CharField(verbose_name='性别', help_text='性别', max_length=6, blank=False, unique=False, null=False,
                                   choices=(('男', '男'), ('女', '女')), default='男')
    phone = models.CharField(verbose_name='手机号', help_text='手机号', max_length=11, blank=True, unique=True, null=True)
    qq = models.CharField(verbose_name='qq号', help_text='qq号', max_length=20, blank=True, unique=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', blank=False, unique=False, null=False, auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', help_text='修改时间', blank=False, unique=False, null=False, auto_now=True)

    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
