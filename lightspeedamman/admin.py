from django.contrib import admin
from .models import TestDrive, CarConfiguration


class TestDriveAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone',
                    'email', 'preferred_date', 'preferred_time')


class CarConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'car_model',
        'package',
        'exterior',
        'interior',
    )

    list_filter = ('car_model', 'user')
    search_fields = ('user__username',)


admin.site.site_header = "Light Speed Amman Admin"
admin.site.site_title = "Light Speed Amman Admin Portal"
admin.site.index_title = "Welcome to Light Speed Amman Researcher Portal"

admin.site.register(TestDrive, TestDriveAdmin)
admin.site.register(CarConfiguration, CarConfigurationAdmin)
