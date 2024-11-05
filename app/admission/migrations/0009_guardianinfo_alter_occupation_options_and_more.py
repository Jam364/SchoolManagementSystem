# Generated by Django 4.2.16 on 2024-11-02 17:17

import app.admission.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0013_course_enrollment'),
        ('admission', '0008_alter_additionalinfo_nationality_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuardianInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(help_text="Enter the guardian's full name.", max_length=100, verbose_name='Guardian Full Name')),
                ('cnic', models.CharField(help_text="Enter the guardian's CNIC.", max_length=15, validators=[app.admission.models.validate_cnic], verbose_name="Guardian's CNIC")),
                ('mobile_number', models.CharField(blank=True, help_text="Enter the guardian's 11-digit mobile number.", max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'Enter a valid 11-digit mobile number.')], verbose_name="Guardian's Mobile Number")),
                ('email', models.EmailField(blank=True, help_text='Enter a valid email address.', max_length=254, null=True, verbose_name="Guardian's Email Address")),
                ('home_address', models.CharField(blank=True, help_text="Enter the guardian's home address.", max_length=255, null=True, verbose_name="Guardian's Home Address")),
                ('office_address', models.CharField(blank=True, help_text="Enter the guardian's office address.", max_length=255, null=True, verbose_name="Guardian's Office Address")),
                ('relation_to_child', models.CharField(choices=[('FATHER', 'Father'), ('MOTHER', 'Mother'), ('GUARDIAN', 'Guardian'), ('OTHER', 'Other')], help_text="Enter the guardian's relation to the child.", max_length=50, verbose_name="Guardian's Relation to Child")),
                ('pick_and_drop', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], help_text='Select if the child needs pick and drop service.', max_length=20, verbose_name='Pick and Drop')),
                ('pick_and_drop_by', models.CharField(blank=True, help_text='Enter the name of the person responsible for pick and drop.', max_length=100, null=True, verbose_name='Pick and Drop By')),
                ('pick_and_drop_cnic', models.CharField(blank=True, help_text='Enter the CNIC of the person responsible for pick and drop.', max_length=15, null=True, validators=[app.admission.models.validate_cnic], verbose_name='Pick and Drop CNIC')),
            ],
        ),
        migrations.AlterModelOptions(
            name='occupation',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveIndex(
            model_name='parentinfo',
            name='guardian_name_idx',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_cnic',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_email',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_full_name',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_home_address',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_mobile_number',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_occupation',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_office_address',
        ),
        migrations.RemoveField(
            model_name='parentinfo',
            name='guardian_relation_to_child',
        ),
        migrations.AddField(
            model_name='academicinfo',
            name='class_required',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='required_class', to='academic.class', verbose_name='Class Required'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='admission_by',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Admitted By'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionalinfo',
            name='other_information',
            field=models.TextField(blank=True, null=True, verbose_name='Other Information'),
        ),
        migrations.AddField(
            model_name='admission',
            name='admission_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20, verbose_name='Admission Status'),
        ),
        migrations.AddField(
            model_name='financialinfo',
            name='advance',
            field=models.PositiveIntegerField(default=0, verbose_name='Advance Payment'),
        ),
        migrations.AddField(
            model_name='financialinfo',
            name='arrears',
            field=models.PositiveIntegerField(default=0, verbose_name='Arrears'),
        ),
        migrations.AddField(
            model_name='financialinfo',
            name='total_arrear_months',
            field=models.PositiveIntegerField(default=0, verbose_name='Total Arrear Months'),
        ),
        migrations.AddField(
            model_name='occupation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='occupation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='parentinfo',
            name='mother_is_alive',
            field=models.BooleanField(default=True, help_text='Indicates if the mother is alive.', verbose_name='Is Mother Alive?'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='child',
            field=models.CharField(blank=True, help_text="Enter the child's full name (if applicable).", max_length=100, null=True, verbose_name="Child's Name"),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='form_b_no',
            field=models.CharField(blank=True, help_text='Enter the Form B number (if applicable).', max_length=50, null=True, verbose_name='Form B Number'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='office_address',
            field=models.CharField(blank=True, help_text='Enter the office address.', max_length=255, null=True, verbose_name='Office Address'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='phone_residence',
            field=models.CharField(blank=True, help_text='Enter the residence phone number.', max_length=15, null=True, verbose_name='Residence Phone Number'),
        ),
        migrations.AddField(
            model_name='guardianinfo',
            name='occupation',
            field=models.ForeignKey(blank=True, help_text="Select guardian's occupation.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='admission.occupation', verbose_name="Guardian's Occupation"),
        ),
        migrations.AddField(
            model_name='admission',
            name='guardian_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admission.guardianinfo', verbose_name='Guardian Information'),
        ),
        migrations.AddIndex(
            model_name='guardianinfo',
            index=models.Index(fields=['full_name'], name='guardian_name_idx'),
        ),
    ]
