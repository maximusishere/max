# Generated by Django 3.2.16 on 2024-06-08 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_text_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='title',
            new_name='name',
        ),
    ]