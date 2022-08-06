from django.contrib import admin
from social.models import Register

# Register your models here.

admin.site.register(Register)


# @admin.register(Register)
# class RegisterAdmin(admin.ModelAdmin):
#     list_display = ['id', 'img', 'date']