from django.contrib import admin
from .models import ToDo
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ["title","body"]
    search_fields = ["title"]

admin.site.register(ToDo,ToDoAdmin)