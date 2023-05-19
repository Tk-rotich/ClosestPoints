from django.contrib import admin
from .models import ClosestPoints

# Register your models here.
@admin.register(ClosestPoints)
class ClosestPointsAdmin(admin.ModelAdmin):
    list_display = ("points", "closest")