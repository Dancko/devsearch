# Generated by Django 4.1.4 on 2022-12-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_project_featured_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="images/default.jpg", null=True, upload_to=""
            ),
        ),
    ]
