# !/usr/bin/python

# -*- coding: utf8 -*-
from django.contrib import admin
from .models import Teacher, Course, Student,InformationCenter,InformationCourse,InformationIndex

# Register your models here.
admin.site.site_header = 'English Center'


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','number_phone','address', 'sex', 'date_birth']
    list_filter = ['name', 'date_birth']
    search_fields = ['name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name_teacher', 'number_phone', 'address', 'subjects']


class InformationCenterAdmin(admin.ModelAdmin):
    list_display = ['center_name', 'hotline', 'address_center']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name_course', 'content']

class InformationIndexAdmin(admin.ModelAdmin):
    list_display = ['title_1', 'title_2', 'title_3']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(InformationCenter, InformationCenterAdmin)
admin.site.register(InformationIndex, InformationIndexAdmin)
admin.site.register(InformationCourse)

