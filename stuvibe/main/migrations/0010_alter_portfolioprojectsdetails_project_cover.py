# Generated by Django 4.2.4 on 2023-09-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_portfolio_portfolio_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioprojectsdetails',
            name='project_cover',
            field=models.ImageField(blank=True, null=True, upload_to='static/data/project_cover'),
        ),
    ]
