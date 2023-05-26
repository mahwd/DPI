# Generated by Django 4.2 on 2023-05-26 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_carousel_left_button_url_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Carousel',
        ),
        migrations.DeleteModel(
            name='InfoTag',
        ),
        migrations.RemoveField(
            model_name='menusubitems',
            name='base_header_item',
        ),
        migrations.RemoveField(
            model_name='menusubitems',
            name='parent_sub_item',
        ),
        migrations.DeleteModel(
            name='MiniSwipe',
        ),
        migrations.DeleteModel(
            name='SectionInfo',
        ),
        migrations.DeleteModel(
            name='ServiceIcon',
        ),
        migrations.DeleteModel(
            name='ServicePlan',
        ),
        migrations.DeleteModel(
            name='MenuBaseItems',
        ),
        migrations.DeleteModel(
            name='MenuSubItems',
        ),
    ]