# Generated by Django 4.2 on 2023-05-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='url',
            field=models.URLField(default='', verbose_name='URL'),
            preserve_default=False,
        ),
    ]
