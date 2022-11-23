from django.contrib import admin
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = 'title', 'photo', 'weight', 'cost'
    list_display_links = 'title', 'photo'
    search_fields = 'title',


admin.site.register(Food, FoodAdmin)
