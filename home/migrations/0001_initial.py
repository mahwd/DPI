# Generated by Django 4.2 on 2023-05-26 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('pretitle', models.CharField(max_length=128, verbose_name='Ön başlıq')),
                ('title', models.CharField(max_length=128, verbose_name='Başlıq')),
                ('description', models.TextField(max_length=512, verbose_name='Açıqlama')),
                ('image', models.ImageField(upload_to='carousel_images/', verbose_name='Karusel şəkli')),
                ('left_button_text', models.CharField(max_length=50, verbose_name='Soldakı düymə mətni')),
                ('left_button_url', models.CharField(max_length=128, verbose_name='Soldakı düymə url-i')),
                ('right_button_text', models.CharField(max_length=50, verbose_name='Sağdakı düymə mətni')),
                ('right_button_url', models.CharField(max_length=128, verbose_name='Sağdakı düymə url-i')),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name': 'Karusel',
                'verbose_name_plural': 'Karusel',
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='InfoTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('title', models.CharField(max_length=255, verbose_name='Teq')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('sort_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name': 'İnfo Teq',
                'verbose_name_plural': 'İnfo Teqlər',
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='MenuBaseItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('title', models.CharField(max_length=128, verbose_name='Menu title')),
                ('order', models.IntegerField(default=0, verbose_name='Menu order')),
                ('url', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Redirect url')),
            ],
            options={
                'verbose_name': 'Əsas menu linki',
                'verbose_name_plural': 'Əsas menu linkləri',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='MiniSwipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('idiom', models.TextField(verbose_name='Mətn')),
                ('author', models.CharField(max_length=100, verbose_name='Müəllif')),
                ('author_profession', models.CharField(max_length=100, verbose_name='Vəzifə')),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='swiper_auther_images', verbose_name='Şəkil')),
            ],
            options={
                'verbose_name': 'Mini Swiper',
                'verbose_name_plural': 'Swipers',
            },
        ),
        migrations.CreateModel(
            name='SectionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('section', models.CharField(choices=[('welcome', 'Welcome section'), ('video', 'Video section'), ('service', 'Services section'), ('info', 'Info section'), ('testimonials', 'Testimonials section'), ('projects', 'Projects section'), ('team', 'Our team section'), ('special_offer', ' Offer section')], max_length=255, verbose_name='Section seçin')),
                ('pretitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ön başlıq')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlıq')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıqlama')),
                ('button_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Düymə mətni')),
                ('button_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Düymə url-i')),
                ('secondary_button_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Əlavə düymə mətni')),
                ('secondary_button_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Əlavə düymə url-i')),
                ('video_source', models.TextField(blank=True, null=True, verbose_name='Video mənbə kodu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='section_images', verbose_name='Şəkil')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='section_images', verbose_name='Əlavə şəkil ')),
            ],
            options={
                'verbose_name': 'Section Information',
                'verbose_name_plural': 'Section Information',
            },
        ),
        migrations.CreateModel(
            name='ServiceIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('title', models.CharField(max_length=128, verbose_name='Servis adı')),
                ('url', models.CharField(max_length=255, verbose_name='Servis URL-i')),
                ('type', models.CharField(choices=[('mini', 'Kiçik'), ('middle', 'Orta')], max_length=64, verbose_name='Servis tipi')),
                ('icon', models.CharField(blank=True, max_length=128, null=True, verbose_name='Servis ikon klası')),
                ('image', models.ImageField(blank=True, null=True, upload_to='section_images', verbose_name='Servis şəkli')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Servis açıqlaması')),
            ],
            options={
                'verbose_name': 'Servis ikonu',
                'verbose_name_plural': 'Servis ikonları',
            },
        ),
        migrations.CreateModel(
            name='ServicePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('title', models.CharField(max_length=255, verbose_name='Planın adı')),
                ('description', models.CharField(max_length=255, verbose_name='Planın açıqlaması')),
                ('price', models.CharField(max_length=255, verbose_name='Planın qiyməti')),
                ('currency', models.CharField(max_length=255, verbose_name='Plan qiymətinin valyutası')),
            ],
            options={
                'verbose_name': 'Servis paketi',
                'verbose_name_plural': 'Servis paketləri',
            },
        ),
        migrations.CreateModel(
            name='MenuSubItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dəyişdirilmə tarixi')),
                ('active', models.BooleanField(default=True, verbose_name='Aktivdirmi')),
                ('title', models.CharField(max_length=128, verbose_name='Menu title')),
                ('url', models.CharField(max_length=255, verbose_name='Redirect url')),
                ('order', models.IntegerField(default=0, verbose_name='Menu order')),
                ('base_header_item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subitems', to='home.menubaseitems', verbose_name='Parent header menu')),
                ('parent_sub_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.menusubitems', verbose_name='Parent menu')),
            ],
            options={
                'verbose_name': 'Köməkçi menu linki',
                'verbose_name_plural': 'Köməkçi menu linkləri',
                'ordering': ('order',),
            },
        ),
    ]
