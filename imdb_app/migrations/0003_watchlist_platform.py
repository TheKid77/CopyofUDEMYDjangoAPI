# Generated by Django 3.1.12 on 2021-06-17 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0002_auto_20210617_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='imdb_app.streamplatform'),
        ),
    ]
