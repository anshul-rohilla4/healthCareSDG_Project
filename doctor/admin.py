from django.contrib import admin
from doctor.models import DoctorInfo
from django.contrib.auth.models import User

@admin.register(DoctorInfo)
class DoctorInfoAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'department']
    list_filter = ['department']
    search_fields = ['user__first_name', 'user__last_name', 'department', 'user__username']
    raw_id_fields = ['user']

    def get_name(self, obj):
        username = obj.user.username
        first_name = obj.user.first_name or username
        last_name = obj.user.last_name or ""
        return f"Dr. {first_name} {last_name} ({username})"
    get_name.short_description = 'Doctor Name'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
