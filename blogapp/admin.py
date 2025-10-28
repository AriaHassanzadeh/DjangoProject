from django.contrib import admin
from .models import Category , Blog , Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_field = {"slug":("title",)}


admin.site.register(Blog , BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)
