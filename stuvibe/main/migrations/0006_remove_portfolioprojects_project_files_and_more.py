# Generated by Django 4.2.4 on 2023-09-12 05:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_portfolioprojectsdetails_project_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioprojects',
            name='project_files',
        ),
        migrations.AlterField(
            model_name='portfolioprojectsdetails',
            name='project_files',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
