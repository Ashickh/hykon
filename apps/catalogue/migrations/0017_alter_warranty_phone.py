# Generated by Django 3.2.18 on 2023-05-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_alter_warranty_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
