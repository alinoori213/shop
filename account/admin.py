from django.contrib import admin

from .models import UserBase, Discount

admin.site.register(UserBase)
admin.site.register(Discount)
