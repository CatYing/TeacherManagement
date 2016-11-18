from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import *


# Register your models here.
class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(StudentInfo)