# Generated by Django 4.2.16 on 2024-11-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_category_options_alter_province_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nationality',
            name='title',
        ),
        migrations.RemoveField(
            model_name='province',
            name='title',
        ),
        migrations.AddField(
            model_name='nationality',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='religion',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
