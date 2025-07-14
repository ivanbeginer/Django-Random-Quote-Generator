from django.contrib import admin

from viewer.models import Viewer

# Register your models here.
class ViewerAdmin(admin.ModelAdmin):
    list_display = ['ip_address','watched_quotes','liked_quotes','disliked_quotes']



admin.site.register(Viewer,ViewerAdmin)