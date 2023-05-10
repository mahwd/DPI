# Generated by Django 4.2 on 2023-05-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_miniswipe_section_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='menubaseitems',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='menusubitems',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='miniswipe',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='sectioninfo',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='serviceicon',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='socialmediaicon',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
        migrations.AddField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=False, verbose_name='dəyişdirilmə tarixi'),
        ),
    ]
