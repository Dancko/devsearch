# Generated by Django 4.1.4 on 2022-12-13 13:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="vote_ratio",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="vote_total",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("body", models.CharField(max_length=500)),
                (
                    "value",
                    models.CharField(
                        choices=[("Up", "Up vote"), ("Down", "Down vote")],
                        max_length=200,
                    ),
                ),
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
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]