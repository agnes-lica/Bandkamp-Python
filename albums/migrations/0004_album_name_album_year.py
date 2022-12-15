# Generated by Django 4.0.7 on 2022-12-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_remove_album_name_remove_album_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(default=2000, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
            preserve_default=False,
        ),
    ]