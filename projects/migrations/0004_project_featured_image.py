# Generated by Django 4.1.4 on 2022-12-14 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_tag_project_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="images/default.svg", null=True, upload_to=""
            ),
        ),
    ]
