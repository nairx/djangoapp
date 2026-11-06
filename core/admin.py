from django.contrib import admin

# Register your models here.
from core.models import todo,product

class todoadmin(admin.ModelAdmin):
    list_display=('task',)

admin.site.register(todo,todoadmin)


class productadmin(admin.ModelAdmin):
    list_display=('name','price','desc','imageUrl')

admin.site.register(product,productadmin)


