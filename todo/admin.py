from django.contrib import admin
from .models import Item

# from the current directories models file import the 'Item' class
# Register your models here.
admin.site.register(Item)
#registers the Item model