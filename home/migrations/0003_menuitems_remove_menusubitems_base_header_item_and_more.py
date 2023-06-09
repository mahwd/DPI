# Generated by Django 4.2 on 2023-05-26 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_menusubitems_base_header_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('title', models.CharField(max_length=128, verbose_name='Menu title')),
                ('order', models.IntegerField(default=0, verbose_name='Menu order')),
                ('url', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Redirect url')),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.menuitems', verbose_name='Parent menu')),
            ],
            options={
                'verbose_name': 'Menu linki',
                'verbose_name_plural': 'Menu linkləri',
                'ordering': ['sort_order'],
            },
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
            name='MenuBaseItems',
        ),
        migrations.DeleteModel(
            name='MenuSubItems',
        ),
    ]
