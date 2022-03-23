from django.contrib import admin
from .models import Todo
from .models import Image
# from .models import Automobiles

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'header_image', 'completed')

# class AutomobilesAdmin(admin.ModelAdmin):
#     list_display1 = ('Automobiles')
# # Register your models here.

admin.site.register(Todo, TodoAdmin)
admin.site.register(Image)
# admin.site.register(Automobiles, AutomobilesAdmin)
