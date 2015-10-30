from django.contrib import admin
from web.models import Web

class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'view_count', 'created_at')
    list_filter = ('title', 'author')

admin.site.register(Web, WebAdmin)
