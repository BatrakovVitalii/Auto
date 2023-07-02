from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(AutoComponents)
class AutoAdmin (admin.ModelAdmin):
    list_display = (
        'id', 'title', 'power', 'country', 'drive', 'comment'
    )