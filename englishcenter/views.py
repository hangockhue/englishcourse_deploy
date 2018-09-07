#!/usr/bin/python

# -*- coding: utf8 -*-
from django.shortcuts import render, redirect
from .forms import StudentForm
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Student, Teacher, Course, InformationIndex, InformationCenter
# Create your views here.


def index(request):

    index_information = get_object_or_404(InformationIndex)
    center_information = InformationCenter.objects.get(pk=1)
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
            return render(request, 'englishcenter/index.html')

        except Exception as e:
            raise Http404("Lỗi nhập form đăng ký")

    return render(request, 'englishcenter/index.html', {'index_information': index_information},
                  {'center_information': center_information})


def course(request):
    course_data = get_object_or_404(Course)
    return render(request, 'englishcenter/course.html', {'course_data': course_data})

def about(request):
    return render(request, 'englishcenter/about.html')

def approach(request):
    return render(request, 'englishcenter/approach.html')


def header(request):
    center_information = InformationCenter.objects.get(pk=1)
    return render(request, 'englishcenter/header.html', {'center_information': center_information})

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