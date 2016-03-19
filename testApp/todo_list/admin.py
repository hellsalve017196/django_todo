from django.contrib import admin

# registering models
from todo_list.models import User
from todo_list.models import Todo

class UserAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','full_name']

    class Meta:
        model = User


class TodoAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','t_date']

    class Meta:
        model = Todo

admin.site.register(User,UserAdmin)
admin.site.register(Todo,TodoAdmin)