# Generated by Django 3.2.9 on 2021-11-18 08:20

from django.db import migrations, models
import miniinsta.models


class Migration(migrations.Migration):

    dependencies = [
        ('miniinsta', '0003_alter_albums_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=miniinsta.models.upload_to),
        ),
    ]