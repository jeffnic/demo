from django.contrib import admin
from .models import Person




# class AuthorAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Person)
