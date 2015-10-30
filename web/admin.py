from django.contrib import admin
from web.models import Web

class WebAdmin(admin.ModelAdmin):
    pass

admin.site.register(Web, WebAdmin)
