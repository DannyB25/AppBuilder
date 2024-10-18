from django.contrib import admin
from .models import HappyPlace

# Register your models here.
@admin.register(HappyPlace) #registers HappyPlace model within Django admin site. A shortcut admin.site.register(HappyPlace, HappyPlaceAdmin)
class HappyPlaceAdmin(admin.ModelAdmin): #defines how the model is represented in the Django admin interface
    list_display = ('f_name', 'l_name', 'location', 'created_at') #defines the fields to be displayed as columns in the list view of the model
    search_fields = ('f_name', 'l_name', 'location') #determines which fields are searchable
    ordering = ('created_at',) #the order of returned values are dependent on when the values were inputted


