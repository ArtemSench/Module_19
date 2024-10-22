from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buyer)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title',)
    list_filter = ('cost', 'description',)
    fieldsets = (
        ('info',{
            'fields':
                ('title', 'cost', 'size')
        }),
        ('footer',{
            'fields':
                ('description', 'age_limited')
        }),
    )