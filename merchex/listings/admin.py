from django.contrib import admin
from listings.models import Band,listing
# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band,BandAdmin)
admin.site.register(listing)