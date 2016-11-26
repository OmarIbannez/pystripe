from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'plan',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (('Personal info'), {
            'fields': (('first_name', 'middle_name', 'last_name'), 'photo', 'email',)
        }),
        (('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
        (('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'photo',
                'password1',
                'password2'
            )
        }),
    )

admin.site.register(User, CustomUserAdmin)
