from django.contrib import admin
from .models import Court

# Register your models here.
class CourtAdmin(admin.ModelAdmin):
  list_display = ("name", "surface", "location",)

admin.site.register(Court, CourtAdmin)

# admin.site.register(Member)


