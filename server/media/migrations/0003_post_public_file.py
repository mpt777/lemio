# Generated by Django 5.0.4 on 2024-04-28 23:15

import media.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_remove_post_video_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public_file',
            field=models.FileField(blank=True, null=True, upload_to=media.models.public_handle_uploaded_file),
        ),
    ]
