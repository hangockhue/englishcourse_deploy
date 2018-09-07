#!/usr/bin/python

# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Student, Teacher, Course, InformationIndex
# Create your views here.


def index(request):

    index_information = get_object_or_404(InformationIndex)

    if request.method == "POST":
        try:
            student_name = request.POST['student_name']
            email = request.POST['email']
            numberphone = request.POST['numberphone']
            address = request.POST['address']
            sex = request.POST['sex']
            datebirth = request.POST['datebirth']

            student_form = Student(name=student_name, email=email, number_phone=numberphone,
                                   address=address, sex=sex, date_birth=datebirth)
            student_form.save()
            return render(request, 'englishcenter/index.html.html')

        except Exception as e:
            raise Http404("Lỗi nhập form đăng ký")

    return render(request, 'englishcenter/index.html', {'index_information': index_information})


def course(request):
    course_data = get_object_or_404(Course)
    return render(request, 'englishcenter/course.html', {'course_data': course_data})


def index_information(request):
    return True


def register(request):
    if request.method == 'POST':
        try:
            student_name = request.POST['student_name']
            email = request.POST['email']
            numberphone = request.POST['numberphone']
            address = request.POST['address']
            sex = request.POST['sex']
            datebirth = request.POST['datebirth']

            student_form = Student(name=student_name, email=email, number_phone=numberphone,
                               address=address, sex=sex,date_birth=datebirth)
            student_form.save()
            return render(request, 'englishcenter/register.html')

        except Exception as e:
            raise Http404("Lỗi nhập form đăng ký")
    return render(request, 'englishcenter/register.html')