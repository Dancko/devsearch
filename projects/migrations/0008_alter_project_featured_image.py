# Generated by Django 4.1.4 on 2022-12-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0007_alter_project_featured_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]