from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(verbose_name="Foydalnuvchi telegram_ID", blank=True, null=True, unique=True)
    username = models.CharField(max_length=250, verbose_name="Foydalanuvchi Username", blank=True, null=True)
    first_name = models.CharField(max_length=250, verbose_name="Foydalanuvchi first_name", blank=True, null=True)
    ism_fam = models.CharField(max_length=50, verbose_name="Foydalanuvchi ism familyasi", blank=True, null=True)
    phone_number = models.CharField(max_length=50, verbose_name="Foydalnuvchi raqami", blank=True, null=True)
    language = models.CharField(max_length=50, verbose_name="Foydalanuvchi tili", blank=True, null=True)
    user_tarif = models.CharField(max_length=50, verbose_name="Foydalanuvchi tarifi", default="Tarif mavjud emas")
    is_active = models.BooleanField(default=False, verbose_name="Foydalanuvchi activligi", blank=True, null=True)
    active_tarif_user_start = models.DateTimeField(null=True, blank=True)
    active_tarif_user_end = models.DateTimeField(null=True, blank=True)
    tarif_end = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return str(self.telegram_id)


class Tarif(models.Model):
    tarif_name = models.CharField(max_length=25, verbose_name="Tariflar")
    tarif_price = models.IntegerField(verbose_name="Tarif narxi")
    tarif_active_date = models.DateTimeField(auto_now_add=True)
    references = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tariflar"

    def __str__(self):
        return self.tarif_name
