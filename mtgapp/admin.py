from django.contrib import admin

# Register your models here.
from .models import Card, Card_Type, Card_Sub_Type

admin.site.register(Card)
admin.site.register(Card_Type)
admin.site.register(Card_Sub_Type)