from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'slug',)
    list_display = (
        'id', 'title', 'description', 'slug',
        'is_published', 'created_at',)
    list_display_links = ('title', 'slug',)
    list_editable = ('is_published', 'description',)
    list_filter = ('created_at',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'id', 'name', 'created_at', 'is_published',
    )
    list_display_links = ('name',)
    list_editable = ('is_published',)
    list_filter = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    list_display = (
        'id', 'title', 'author', 'text', 'category', 'pub_date',
        'location', 'is_published', 'created_at',
    )
    list_display_links = ('title',)
    list_editable = ('category', 'is_published', 'location',)
    list_filter = ('created_at',)
    empty_value_distplay = '-пусто-'
