# Generated by Django 4.1.1 on 2022-09-16 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_alter_content_options_alter_module_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="module",
            old_name="courses",
            new_name="course",
        ),
    ]