from django.contrib import admin
from app.models import *

# Register your models here.

class CUSTOMIZEUser(admin.ModelAdmin):
    list_display=['User_ID','User_name','Email']
    list_display_links=['User_ID','User_name']
    list_editable=['Email']
    # list_filter=['name']
    # list_per_page=3

admin.site.register(User,CUSTOMIZEUser)

admin.site.register(Order)

admin.site.register(Books)


admin.side.site()