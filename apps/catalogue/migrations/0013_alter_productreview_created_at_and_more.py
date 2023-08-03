# Generated by Django 4.1.2 on 2023-04-19 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_alter_warranty_contact_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.productvariant'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
