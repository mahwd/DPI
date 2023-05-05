# Generated by Django 4.2 on 2023-05-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_videosection_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='dəyişdirilmə tarixi')),
                ('pretitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ön başlıq')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlıq')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıqlama')),
                ('button_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Düymə mətni')),
                ('button_url', models.URLField(blank=True, null=True, verbose_name='Düymə url-i')),
                ('video_source', models.TextField(blank=True, null=True, verbose_name='Video mənbə kodu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='video_section_image', verbose_name='Video cover')),
                ('section', models.CharField(choices=[('welcome', 'Welcome section'), ('video', 'Video section'), ('service', 'Services section'), ('info', 'Info section'), ('testimonials', 'Testimonials section'), ('projects', "'OUR PROJECTS' section")], max_length=255, verbose_name='Section seçin')),
            ],
            options={
                'verbose_name': 'Section Information',
                'verbose_name_plural': 'Section Information',
            },
        ),
        migrations.DeleteModel(
            name='VideoSection',
        ),
        migrations.DeleteModel(
            name='WelcomeSection',
        ),
    ]
