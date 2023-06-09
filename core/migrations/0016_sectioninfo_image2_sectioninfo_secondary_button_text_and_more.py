# Generated by Django 4.2 on 2023-05-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_sectioninfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectioninfo',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='section_images', verbose_name='Əlavə şəkil '),
        ),
        migrations.AddField(
            model_name='sectioninfo',
            name='secondary_button_text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Əlavə düymə mətni'),
        ),
        migrations.AddField(
            model_name='sectioninfo',
            name='secondary_button_url',
            field=models.URLField(blank=True, null=True, verbose_name='Əlavə düymə url-i'),
        ),
    ]
