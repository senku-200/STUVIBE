# Generated by Django 4.2.4 on 2023-09-12 04:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_messages_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioprojects',
            name='project_files',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
