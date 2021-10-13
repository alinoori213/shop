from django.contrib import admin

from .models import UserBase, Discount


# class TestAdminPermissions(admin.ModelAdmin):
#
#     def has_add_permission(self, request):
#         return False
#     def has
admin.site.register(UserBase)
admin.site.register(Discount)
