# Generated by Django 4.1.4 on 2022-12-13 13:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_vote_ratio_project_vote_total_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="tags",
            field=models.ManyToManyField(blank=True, to="projects.tag"),
        ),
    ]