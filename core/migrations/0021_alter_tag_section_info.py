# Generated by Django 4.2 on 2023-05-08 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_tag_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='section_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='core.sectioninfo', verbose_name='Bölmə'),
        ),
    ]