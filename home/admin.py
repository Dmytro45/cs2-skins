from django.contrib import admin

from home.models import Car, Mark, Color, Drive, Model

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
   list_display = ['name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
   list_display = ['name']

@admin.register(Drive)
class ColorAdmin(admin.ModelAdmin):
   list_display = ['name']
   
@admin.register(Model)
class ColorAdmin(admin.ModelAdmin):
   list_display = ['name']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
   list_display = ['mark', 'model', 'price', 'color','year','drive']
   list_filter = ['mark',]