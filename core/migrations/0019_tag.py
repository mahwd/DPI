# Generated by Django 4.2 on 2023-05-08 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_serviceicon_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='dəyişdirilmə tarixi')),
                ('title', models.CharField(max_length=255, verbose_name='Teq')),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('section_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sectioninfo', verbose_name='Bölmə')),
            ],
            options={
                'verbose_name': 'Teq',
                'verbose_name_plural': 'Teqlər',
                'ordering': ['sort_order'],
            },
        ),
    ]