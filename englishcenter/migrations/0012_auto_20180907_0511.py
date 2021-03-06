# Generated by Django 2.1 on 2018-09-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishcenter', '0011_auto_20180907_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informationindex',
            old_name='information_3',
            new_name='content_title_3',
        ),
        migrations.RenameField(
            model_name='informationindex',
            old_name='information_4',
            new_name='content_title_4',
        ),
        migrations.AlterField(
            model_name='informationindex',
            name='slide_picture_1',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='informationindex',
            name='slide_picture_2',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='informationindex',
            name='slide_picture_3',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
