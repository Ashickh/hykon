# Generated by Django 4.1.2 on 2023-04-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_ordertracking_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='placed',
            field=models.BooleanField(default=False),
        ),
    ]
