from django.contrib import admin
from .models import Blog 
from .models import Category,Tag,Comments
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)
class BlogAdmin(admin.ModelAdmin):
    list_display=("title","created_at","author")
    list_filter=("title",)
    search_fields=("title",)
    ordering=("title","author")
    date_hierarchy="created_at"

admin.site.register(Blog,BlogAdmin)