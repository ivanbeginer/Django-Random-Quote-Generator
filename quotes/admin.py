from django.contrib import admin

from quotes.models import Source, Quote

# Register your models here.
class SourceAdmin(admin.ModelAdmin):
    list_display = ['name','author','year','type']

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text','source','weight','views','likes','dislikes']


    
    
admin.site.register(Source,SourceAdmin)
admin.site.register(Quote,QuoteAdmin)
