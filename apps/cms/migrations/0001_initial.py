# Generated by Django 4.1.1 on 2023-03-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activitie',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('request_token', models.CharField(blank=True, max_length=255, null=True)),
                ('guest_id', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('response_http_code', models.CharField(blank=True, max_length=255, null=True)),
                ('response_time', models.CharField(blank=True, max_length=255, null=True)),
                ('response', models.TextField(blank=True, null=True)),
                ('payload', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'activities',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AdminPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('permission', models.CharField(max_length=250)),
                ('target', models.CharField(blank=True, max_length=10, null=True)),
                ('icon', models.CharField(max_length=50)),
                ('parent', models.IntegerField()),
                ('display_order', models.IntegerField()),
                ('created_by', models.BigIntegerField()),
                ('updated_by', models.BigIntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'admin_pages',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('banner_name', models.CharField(max_length=250)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('code', models.CharField(max_length=250)),
                ('width', models.SmallIntegerField(blank=True, null=True)),
                ('height', models.SmallIntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'banners',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BannerPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('crop_data', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('alt_text', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'banner_photos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bannable_type', models.CharField(max_length=191)),
                ('created_by_type', models.CharField(blank=True, max_length=191, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bans',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BranchData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=46, null=True)),
                ('city', models.CharField(blank=True, max_length=91, null=True)),
                ('district', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=11, null=True)),
                ('mobile', models.CharField(blank=True, max_length=35, null=True)),
                ('contact', models.CharField(blank=True, max_length=13, null=True)),
            ],
            options={
                'db_table': 'brach_data',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=7)),
                ('location', models.CharField(max_length=250)),
                ('branch_name', models.CharField(max_length=250)),
                ('page_heading', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=191, null=True)),
                ('landline_number', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_person_number', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_person_image', models.IntegerField(blank=True, null=True)),
                ('gstin', models.CharField(blank=True, db_column='GSTIN', max_length=45, null=True)),
                ('lattitude', models.CharField(blank=True, max_length=191, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('sunday_open', models.IntegerField()),
                ('browser_title', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'branches',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BranchLandmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('landmark', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'branch_landmarks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FrontendPage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('browser_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('top_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('bottom_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('extra_css', models.CharField(blank=True, max_length=1000, null=True)),
                ('extra_js', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'frontend_pages',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HomePageSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'home_page_settings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('position', models.CharField(max_length=255)),
                ('menu_type', models.IntegerField()),
                ('menu_order', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menus',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('original_title', models.CharField(blank=True, max_length=255, null=True)),
                ('menu_type', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('menu_nextable_id', models.CharField(blank=True, max_length=255, null=True)),
                ('linkable_type', models.CharField(blank=True, max_length=191, null=True)),
                ('linkable_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('menu_order', models.IntegerField()),
                ('parent_id', models.BigIntegerField()),
                ('target_blank', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu_items',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=250)),
                ('unsubscribed', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'newsletter_subscriptions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=191)),
                ('token', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'password_resets',
                'managed': True,
            },
        ),
    ]