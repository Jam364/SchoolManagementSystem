# Generated by Django 5.1.1 on 2024-10-18 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
        ('common', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=3)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('current_address', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('general_health', models.CharField(max_length=255)),
                ('immunization', models.CharField(max_length=255)),
                ('disabilities', models.CharField(max_length=255)),
                ('mark_of_identification', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AcademicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admission_no', models.CharField(max_length=20)),
                ('admission_type', models.CharField(max_length=50)),
                ('admission_confirmation_date', models.DateField()),
                ('marks_in_previous_school', models.PositiveIntegerField()),
                ('previous_school_roll_no', models.CharField(max_length=20)),
                ('enrollment_status', models.CharField(max_length=50)),
                ('test_passed', models.BooleanField(default=False)),
                ('admission_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.class')),
                ('admission_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.section')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_act', models.CharField(max_length=255)),
                ('sibling', models.TextField()),
                ('other_information', models.CharField(max_length=255)),
                ('remarks', models.TextField()),
                ('is_alive', models.BooleanField(default=True)),
                ('is_security_voucher_generated', models.BooleanField(default=False)),
                ('is_voucher_generated', models.BooleanField(default=False)),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.nationality')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.religion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinancialInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fee_remaining_for_months', models.PositiveIntegerField()),
                ('monthly_income', models.PositiveIntegerField()),
                ('paid_dues_upto_slc', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('father_full_name', models.CharField(max_length=100)),
                ('father_cnic', models.CharField(max_length=15)),
                ('mother_full_name', models.CharField(max_length=100)),
                ('mother_cnic', models.CharField(max_length=15)),
                ('mother_mobile_number', models.CharField(max_length=15)),
                ('mother_email', models.EmailField(max_length=254)),
                ('mother_office_address', models.CharField(max_length=255)),
                ('guardian_full_name', models.CharField(max_length=100)),
                ('guardian_cnic', models.CharField(max_length=15)),
                ('guardian_mobile_number', models.CharField(max_length=15)),
                ('guardian_email', models.EmailField(max_length=254)),
                ('guardian_home_address', models.CharField(max_length=255)),
                ('guardian_office_address', models.CharField(max_length=255)),
                ('guardian_relation_to_child', models.CharField(max_length=50)),
                ('father_occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentinfo_father_occupation', to='common.category')),
                ('guardian_occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentinfo_guardian_occupation', to='common.category')),
                ('mother_occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentinfo_mother_occupation', to='common.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admission_by', models.CharField(max_length=100)),
                ('admission_confirmation_date', models.DateField()),
                ('admission_no', models.CharField(max_length=20)),
                ('admission_type', models.CharField(max_length=50)),
                ('academic_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.academicinfo')),
                ('additional_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.additionalinfo')),
                ('financial_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.financialinfo')),
                ('parent_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.parentinfo')),
                ('personal_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.personalinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
