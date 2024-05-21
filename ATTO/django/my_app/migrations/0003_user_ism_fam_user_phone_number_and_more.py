# Generated by Django 5.0.3 on 2024-03-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_tarif_references'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ism_fam',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Foydalanuvchi ism familyasi'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Foydalnuvchi raqami'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Foydalnuvchi telegram_ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_tarif',
            field=models.CharField(default='Tarif mavjud emas', max_length=50, verbose_name='Foydalanuvchi tarifi'),
        ),
    ]
