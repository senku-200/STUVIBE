# Generated by Django 4.2.4 on 2023-09-04 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_portfolio_portfolioprojectsdetails_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='portfolio_projects',
            new_name='PortfolioProjects',
        ),
    ]