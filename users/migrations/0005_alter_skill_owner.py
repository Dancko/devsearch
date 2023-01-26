# Generated by Django 4.1.4 on 2022-12-23 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_profile_location_skill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="owner",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
            preserve_default=False,
        ),
    ]