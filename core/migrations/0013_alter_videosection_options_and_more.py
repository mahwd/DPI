# Generated by Django 4.2 on 2023-05-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_videosection_welcomesection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videosection',
            options={'verbose_name': 'Video Section', 'verbose_name_plural': 'Video Section'},
        ),
        migrations.AlterModelOptions(
            name='welcomesection',
            options={'verbose_name': 'Welcome Section', 'verbose_name_plural': 'Welcome Section'},
        ),
        migrations.AlterField(
            model_name='videosection',
            name='video_source',
            field=models.TextField(verbose_name='Video mənbə kodu'),
        ),
    ]