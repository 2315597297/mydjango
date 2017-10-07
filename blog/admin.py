from django.contrib import admin
from .models import Blog, Bankuai, Leixing, Pinglun

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =('id','title','bankuai','leixing')

@admin.register(Bankuai)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Leixing)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Pinglun)
class BlogAdmin(admin.ModelAdmin):
    list_display =('id','plzhe','plblog')



