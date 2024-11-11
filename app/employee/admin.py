
from django.contrib import admin
from .models import EmployeeDesignation, Employee, StaffPerformance, Qualification

@admin.register(EmployeeDesignation)
class EmployeeDesignationAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'description')
    search_fields = ('name', 'department')
    list_filter = ('department',)
    ordering = ('name',)


    # Restrict add, change, and delete to superusers
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'designation', 'employee_status', 'date_of_joining', 'date_of_resignation')
    search_fields = ('employee_name', 'employee_id', 'cnic', 'email')
    list_filter = ('employee_status', 'designation', 'date_of_joining', 'date_of_resignation')
    date_hierarchy = 'date_of_joining'
    ordering = ('-date_of_joining',)

    fieldsets = (
        (None, {
            'fields': ('employee_name', 'employee_id', 'designation', 'employee_pay_structure')
        }),
        ('Personal Information', {
            'fields': ('date_of_birth', 'gender', 'martial_status', 'contact_no', 'email', 'address', 'city', 'province', 'country')
        }),
        ('Employment Details', {
            'fields': ('date_of_joining', 'date_of_rejoining', 'date_of_resignation', 'employee_status', 'is_verified', 'covid_vaccinated')
        }),
        ('Bank Details', {
            'fields': ('bank', 'account_no')
        }),
        ('Family Information', {
            'fields': ('father_name', 'father_cnic')
        }),
        ('Additional Information', {
            'fields': ('note',)
        }),
    )

    # Restrict add, change, and delete to superusers
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(StaffPerformance)
class StaffPerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating', 'date_evaluated')
    search_fields = ('employee__employee_name',)
    list_filter = ('rating', 'date_evaluated')
    date_hierarchy = 'date_evaluated'
    ordering = ('-date_evaluated',)

    # Restrict add, change, and delete to superusers
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee', 'discipline', 'institution', 'year_obtained')
    search_fields = ('name', 'employee__username', 'discipline', 'institution')
    list_filter = ('year_obtained', 'discipline', 'institution')
    ordering = ('-year_obtained',)

     # Restrict add, change, and delete to superusers
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
