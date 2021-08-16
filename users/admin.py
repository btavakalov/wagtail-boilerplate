from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('__str__', 'is_staff', 'is_active', 'is_superuser', 'last_login')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)


admin.site.register(User, CustomUserAdmin)
