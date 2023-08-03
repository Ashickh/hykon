# Generated by Django 4.1.2 on 2023-05-09 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_alter_warranty_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('mail', models.EmailField(max_length=254)),
                ('place', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=13)),
                ('requirement', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'enquiry',
                'managed': True,
            },
        ),
    ]