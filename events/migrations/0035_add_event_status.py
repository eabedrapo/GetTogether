# Generated by Django 2.0 on 2018-06-23 15:24

from django.db import migrations, models

import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [("events", "0034_add_imagekit_team_cover_img")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="status",
            field=models.SmallIntegerField(
                choices=[(-1, "Canceled"), (0, "Planning"), (1, "Confirmed")],
                db_index=True,
                default=1,
            ),
        )
    ]
