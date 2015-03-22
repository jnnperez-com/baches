from django.contrib import admin

from .models import Reporte

class ReporteyAdmin(admin.ModelAdmin):
	search_fields =('name',)

admin.site.register(Reporte, ReporteyAdmin)