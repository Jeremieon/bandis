# Generated by Django 4.1.3 on 2022-11-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0003_band_active_band_biography_band_genre_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="description",
            field=models.CharField(default="show time", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="sold",
            field=models.IntegerField(default=156),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="type",
            field=models.CharField(
                choices=[
                    ("Rec", "Records"),
                    ("Cloth", "Clothing"),
                    ("poster", "Posters"),
                    ("other", "Miscellaneous"),
                ],
                default="other",
                max_length=15,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="year",
            field=models.DateTimeField(default="2011-09-01T13:20:30+03:00"),
            preserve_default=False,
        ),
    ]
