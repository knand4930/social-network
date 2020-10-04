from django.contrib import admin

# Register your models here.
from .models import Profile, RelationShip


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user', 'updated', 'created']


admin.site.register(Profile, ProfileAdmin)


class RelationShipAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'status', 'updated', 'created']


admin.site.register(RelationShip, RelationShipAdmin)
