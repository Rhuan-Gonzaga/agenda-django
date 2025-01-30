from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #tuplas
    list_display = 'id', 'first_name', 'last_name', 'phone','category','show',
    ordering = '-id',; 
    #list_filter = 'created_date',
    search_fields = 'first_name', 'last_name',
    #list_per_page = 1
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name','show',
    list_display_links = 'id',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    #tuplas
    list_display = 'name',
    ordering = '-id',
    