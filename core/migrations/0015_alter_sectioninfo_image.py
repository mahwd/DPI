# Generated by Django 4.2 on 2023-05-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_sectioninfo_delete_videosection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioninfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='section_images', verbose_name='Şəkil'),
        ),
    ]
