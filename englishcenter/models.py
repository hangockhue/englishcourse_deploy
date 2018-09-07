#!/usr/bin/python

# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.db import models
import os
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from englishcourse import settings

# -- coding: utf-8
# Create your models here.


class InformationIndex(models.Model):

    title_1 = models.CharField(max_length=100, null=True)
    content_title_1 = models.TextField(null=True)

    title_2 = models.CharField(max_length=100, null=True)
    content_title_2 = models.TextField(null=True)

    title_3 = models.CharField(max_length=100, null=True)
    content_title_3 = models.TextField(null=True)

    title_4 = models.CharField(max_length=100, null=True)
    content_title_4 = models.TextField(null=True)

    def __str__(self):
        return self.title_1

    def save(self, *args, **kwargs):
        try:
            # Delete old images when changing
            this = InformationIndex.objects.get(id=self.id)
            if this.slide_picture_1 != self.slide_picture_1:
                delete_picture_path = os.path.join(settings.BASE_DIR, 'media', this.slide_picture_1)
                os.remove(delete_picture_path)
            if this.slide_picture_2 != self.slide_picture_2:
                delete_picture_path = os.path.join(settings.BASE_DIR, 'media', this.slide_picture_2)
                os.remove(delete_picture_path)
            if this.slide_picture_1 != self.slide_picture_1:
                delete_picture_path = os.path.join(settings.BASE_DIR, 'media', this.slide_picture_1)
                os.remove(delete_picture_path)
        except: pass
        super().save(*args, **kwargs)


@receiver(pre_delete, sender=InformationIndex)
def receiver_function(sender, instance, **kwargs):
    # File Image
    delete_img_path = os.path.join(settings.BASE_DIR, 'media', instance.slide_picture_1)
    os.remove(delete_img_path)
    delete_img_path = os.path.join(settings.BASE_DIR, 'media', instance.slide_picture_2)
    os.remove(delete_img_path)
    delete_img_path = os.path.join(settings.BASE_DIR, 'media', instance.slide_picture_3)
    os.remove(delete_img_path)


class InformationCourse(models.Model):
    information_1 = models.TextField()
    information_2 = models.TextField()
    information_3 = models.TextField()


class Student(models.Model):

    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    number_phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    sex_choices = (('Female', 'Female'),
                  ('Male', 'Male')
                  )
    sex = models.CharField(max_length=6, choices=sex_choices)
    date_birth = models.DateTimeField()

    def __str__(self):
        return self.name


class Teacher(models.Model):

    name_teacher = models.CharField(max_length=25)
    image_teacher = models.ImageField(upload_to='images')
    number_phone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    subjects = models.CharField(max_length=100)
    identity_card = models.CharField(max_length=20)
    curriculum_vitae = models.FileField(default='Not Found', upload_to='documents')

    def __str__(self):
        return self.name_teacher

    def save(self, *args, **kwargs):
        try:
            # Delete old images and cv when changing
            this = Teacher.objects.get(id=self.id)
            if this.image_teacher != self.image_teacher:
                delete_img_path = os.path.join(settings.BASE_DIR, 'media', this.image_teacher)
                os.remove(delete_img_path)
            if this.curriculum_vitae != self.curriculum_vitae:
                delete_cv_path = os.path.join(settings.BASE_DIR, 'media', this.curriculum_vitae)
                os.remove(delete_cv_path)
        except: pass
        super().save(*args, **kwargs)


# Delete file and CV when Delete teacher
@receiver(pre_delete, sender=Teacher)
def receiver_function(sender, instance, **kwargs):
    # File image
    delete_img_path = os.path.join(settings.BASE_DIR, 'media', instance.image_teacher.name)
    os.remove(delete_img_path)
    # File CV
    delete_cv_path = os.path.join(settings.BASE_DIR, 'media', instance.curriculum_vitae.name)
    os.remove(delete_cv_path)


class Course(models.Model):

    name_course = models.CharField(max_length=25)
    image_course = models.ImageField(upload_to='images')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    content = models.TextField()
    introduce = models.TextField()
    cost_course = models.CharField(max_length=25, null=True)
    time_open = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name_course

    def save(self, *args, **kwargs):
        try:
            # Delete old image when changing
            this = Course.objects.get(id=self.id)
            if this.image_course != self.image_course:
                delete_img_path = os.path.join(settings.BASE_DIR, 'media', this.image_course)
                os.remove(delete_img_path)
        except: pass
        super().save(*args, **kwargs)


# Delete image course when delete course
@receiver(pre_delete,sender=Course)
def receiver_function(sender, instance, **kwargs):
    # File image
    delete_img_path = os.path.join(settings.BASE_DIR, 'media', instance.image_course.name)
    os.remove(delete_img_path)


class InformationCenter(models.Model):

    center_name = models.CharField(max_length=50, null=True)
    hotline = models.CharField(max_length=11, null=True)
    address_center = models.CharField(max_length=100)

    def __str__(self):
        return self.center_name
