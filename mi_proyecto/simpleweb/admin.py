# simpleweb/admin.py
from django.contrib import admin
from .models import TuModelo

class TuModeloAdmin(admin.ModelAdmin):
    list_display = ('campo1', 'campo2', 'is_deleted')  # Asegúrate de que estos campos existan en TuModelo

admin.site.register(TuModelo, TuModeloAdmin)  # Solo esta línea es necesaria
