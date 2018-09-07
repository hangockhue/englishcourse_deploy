#!/usr/bin/python

# -*- coding: utf8 -*-
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        models = Student
        fields = ['name', 'email', 'number_phone', 'address',
                  'sex', 'date_birth']
