from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title', 'show_photo', 'weight', 'cost'
    list_display_links = 'title', 'show_photo'
    search_fields = 'title', 'pk'

    def show_photo(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='240'/>".format(obj.photo.url))
        else:
            return "None"

    show_photo.__name__ = "Фото"


class PostAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'txt', 'time_create'
    list_display_links = 'pk',
    search_fields = 'name', 'pk'


admin.site.register(Food, FoodAdmin)
admin.site.register(Post)
