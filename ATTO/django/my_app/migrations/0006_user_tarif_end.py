# Generated by Django 5.0.3 on 2024-04-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_rename_active_tarif_user_user_active_tarif_user_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tarif_end',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
