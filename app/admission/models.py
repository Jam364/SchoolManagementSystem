'''from app.common.models import TimeStampedModel
from django.db import models

class admission(TimeStampedModel,models.Model):
    admission_by = models.CharField(max_length=255, default='Unknown')

    admission_confirmation_date = models.DateField()
    admission_no = models.CharField(max_length=50)
    admission_type = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3)
    child = models.CharField(max_length=255)
    computer = models.PositiveIntegerField()
    current_address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    disabilities = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    email = models.EmailField()
    english = models.PositiveIntegerField()
    enrollment_status = models.CharField(max_length=50)
    extra_act = models.CharField(max_length=255)
    father_cnic = models.CharField(max_length=15)
    father_full_name = models.CharField(max_length=255)
    fee_remaining_for_months = models.PositiveIntegerField()
    form_b_no = models.CharField(max_length=15)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    general_health = models.CharField(max_length=255)
    guardian_cnic = models.CharField(max_length=15)
    guardian_email = models.EmailField()
    guardian_full_name = models.CharField(max_length=255)
    guardian_home_address = models.CharField(max_length=255)
    guardian_mobile_number = models.CharField(max_length=15)
    guardian_office_address = models.CharField(max_length=255)
    guardian_relation_to_child = models.CharField(max_length=50)
    immunization = models.CharField(max_length=255)
    is_alive = models.BooleanField(default=True)
    is_security_voucher_generated = models.BooleanField(default=False)
    is_voucher_generated = models.BooleanField(default=False)
    islamiat = models.PositiveIntegerField()
    mark_of_identification = models.CharField(max_length=255)
    marks_in_previous_school = models.PositiveIntegerField()
    maths = models.PositiveIntegerField()
    mobile_number = models.CharField(max_length=15)
    monthly_income = models.PositiveIntegerField()
    mother_cnic = models.CharField(max_length=15)
    mother_education = models.CharField(max_length=255)
    mother_email = models.EmailField()
    mother_full_name = models.CharField(max_length=255)
    mother_is_alive = models.BooleanField(default=True)
    mother_mobile_number = models.CharField(max_length=15)
    mother_office_address = models.CharField(max_length=255)
    mother_office_phone = models.CharField(max_length=15)
    office_address = models.CharField(max_length=255)
    other_information = models.CharField(max_length=255)
    paid_dues_upto_slc = models.DateField()
    permanent_address = models.CharField(max_length=255)
    phone_residence = models.CharField(max_length=15)
    pick_and_drop = models.CharField(max_length=255)
    pick_and_drop_by = models.CharField(max_length=255)
    pick_and_drop_cnic = models.CharField(max_length=15)
    place_of_birth = models.CharField(max_length=255)
    previous_school_roll_no = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    remarks = models.TextField()
    school_address = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    science = models.PositiveIntegerField()
    sibling = models.TextField()
    student_id = models.CharField(max_length=50)
    test_passed = models.BooleanField(default=False)
    urdu = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.full_name} - {self.admission_no}"
        '''
'''from app.common.models import TimeStampedModel
from django.db import models
from django.db.models import Q

class Admission(TimeStampedModel, models.Model):
    admission_by = models.CharField(max_length=255, default='Unknown')
    admission_confirmation_date = models.DateField()
    admission_no = models.CharField(max_length=50, unique=True)
    admission_type = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    guardian_full_name = models.CharField(max_length=255)
    guardian_mobile_number = models.CharField(max_length=15)
    current_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    previous_school_roll_no = models.CharField(max_length=50)
    marks_in_previous_school = models.PositiveIntegerField()
    test_passed = models.BooleanField(default=False)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.admission_no}"

    @classmethod
    def search(cls, query):
        """
        Search for students based on full name, admission number, or mobile number.
        """
        return cls.objects.filter(
            Q(full_name__icontains=query) | 
            Q(admission_no__icontains=query) | 
            Q(mobile_number__icontains=query)
        )
'''