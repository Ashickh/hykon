# Generated by Django 4.1.2 on 2023-03-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_remove_category_is_corporate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='type',
            field=models.CharField(choices=[('Blog', 'Blog'), ('Career', 'Career'), ('Events', 'Events'), ('History', 'History'), ('News', 'News'), ('Page', 'Page')], default='Page', max_length=7),
        ),
    ]
