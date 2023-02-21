from django.contrib import admin
from .models import Owner

# Register your models here.
#admin.site.register(Owner)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("id","nombre", "pais", "edad")
    #list_filter = ("pais",)
    search_fields = ("nombre",)
    fields = ("edad","nombre", "pais", "dni")