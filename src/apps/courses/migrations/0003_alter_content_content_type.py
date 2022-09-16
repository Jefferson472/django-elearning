# Generated by Django 4.1.1 on 2022-09-16 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("courses", "0002_rename_courses_course_video_text_image_file_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to={"model__in": ("text", "video", "image", "file")},
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
    ]
