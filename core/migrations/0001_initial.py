# Generated by Django 4.2 on 2023-05-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuBaseItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Menu title')),
                ('order', models.IntegerField(default=0, verbose_name='Menu order')),
                ('url', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Redirect url')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Header base-menu item',
                'verbose_name_plural': 'Header base-menu items',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='MenuSubItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Menu title')),
                ('url', models.CharField(max_length=255, verbose_name='Redirect url')),
                ('order', models.IntegerField(default=0, verbose_name='Menu order')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('base_header_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.menubaseitems', verbose_name='Parent header menu')),
                ('parent_sub_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.menusubitems', verbose_name='Parent menu')),
            ],
            options={
                'verbose_name': 'Header sub-menu item',
                'verbose_name_plural': 'Header sub-menu items',
                'ordering': ('order',),
            },
        ),
    ]
