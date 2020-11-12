from django.contrib import admin
from .models import Question,choice

admin.site.site_header = "Nautilus Admin"
admin.site.site_title = "Nautilus Admin Area"
admin.site.index_title = "Welcome to Nautilus Admin"

admin.site.register(Question)
admin.site.register(choice)

# Register your models here.
