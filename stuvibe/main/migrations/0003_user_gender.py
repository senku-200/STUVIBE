# Generated by Django 4.0.4 on 2023-08-12 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_post_alter_postdetails_template_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
