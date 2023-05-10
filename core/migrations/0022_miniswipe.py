# Generated by Django 4.2 on 2023-05-08 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_tag_section_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniSwipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='dəyişdirilmə tarixi')),
                ('idiom', models.TextField(verbose_name='Hikmət')),
                ('author', models.CharField(max_length=100, verbose_name='Müəllif')),
                ('author_profession', models.CharField(max_length=100, verbose_name='Vəzifə')),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='swiper_auther_images', verbose_name='Şəkil')),
                ('section_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swipers', to='core.sectioninfo', verbose_name='Bölmə')),
            ],
            options={
                'verbose_name': 'Mini Swiper',
                'verbose_name_plural': 'Swipers',
            },
        ),
    ]
