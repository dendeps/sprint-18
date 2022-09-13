from django.contrib import admin
from authentication.models import CustomUser



class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created_at', 'role', 'is_active')

admin.site.register(CustomUser, UserAdmin)