from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from marks.models import SchoolUser


class SchoolAdmin(UserAdmin):
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    list_display = ('email', 'first_name', 'last_name','is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
         ),
    )


admin.site.register(SchoolUser, SchoolAdmin)