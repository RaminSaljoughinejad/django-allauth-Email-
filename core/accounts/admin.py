from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import NotRegistered

UserModel = get_user_model()

class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = [EmailAddressInline]
    model = UserModel
    list_display = ("email", "is_staff", "is_active", "date_joined")
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email', 'date_joined')
    ordering = ('is_superuser', 'is_staff', 'date_joined')
    readonly_fields = ('date_joined',)

admin.site.register(UserModel, CustomUserAdmin)

admin.site.site_header = 'MyAPP Administration'
admin.site.index_title = "User Management"
admin.site.site_title = 'MyAPP Title'