# Generated by Django 4.1.4 on 2022-12-28 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0011_alter_review_body"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-vote_ratio", "-vote_total", "title"]},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"ordering": ["-created"]},
        ),
    ]
