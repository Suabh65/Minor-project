# Generated by Django 2.2.3 on 2019-07-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_team_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='image',
            field=models.ImageField(null=True, upload_to='tournament_images'),
        ),
    ]
