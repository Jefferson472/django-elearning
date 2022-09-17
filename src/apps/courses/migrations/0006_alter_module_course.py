# Generated by Django 4.1.1 on 2022-09-17 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_rename_courses_module_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="module",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modules",
                to="courses.course",
            ),
        ),
    ]