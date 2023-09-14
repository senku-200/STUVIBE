from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.PostDetails)
admin.site.register(models.Stories)
admin.site.register(models.Portfolio)
admin.site.register(models.PortfolioProjectsDetails)
admin.site.register(models.Message)
