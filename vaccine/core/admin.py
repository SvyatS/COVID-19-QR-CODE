from django.contrib import admin
from .models import UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'surname', 'date_birthday', 'residence_address')
    search_fields = ['first_name', 'middle_name', 'surname']


admin.site.register(UserData, UserDataAdmin)