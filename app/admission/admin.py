'''
from django.contrib import admin
from .models import admission

@admin.register(admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'admission_no', 'admission_type', 'date_of_birth', 'enrollment_status')
    search_fields = ('full_name', 'admission_no', 'guardian_full_name', 'mobile_number')
    list_filter = ('admission_type', 'gender', 'is_alive', 'is_security_voucher_generated', 'is_voucher_generated')
'''
'''''
from django.contrib import admin
from .models import Admission  # Import the Admission model

@admin.register(Admission)  # Use the decorator to register the model
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'admission_no',
        'full_name',
        'date_of_birth',
        'gender',
        'mobile_number',
        'admission_confirmation_date',
        'school_name',
        'test_passed',
    )
    search_fields = ('full_name', 'admission_no', 'mobile_number')
    list_filter = ('gender', 'admission_type', 'test_passed')
    ordering = ('-admission_confirmation_date',)
    list_per_page = 20  # Number of records per page in the admin list view

    # Optionally, customize the form layout
    fieldsets = (
        (None, {
            'fields': (
                'admission_no',
                'full_name',
                'date_of_birth',
                'gender',
                'email',
                'mobile_number',
                'guardian_full_name',
                'guardian_mobile_number',
                'current_address',
                'permanent_address',
                'school_name',
                'previous_school_roll_no',
                'marks_in_previous_school',
                'test_passed',
                'remarks',
                'admission_by',
                'admission_confirmation_date',
                'admission_type',
            )
        }),
    )

'''