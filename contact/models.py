from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Contact(models.Model):
    name=models.CharField(_("نام و نام خانوادگی"),max_length=100)
    email=models.EmailField(_("آدرس الکترونیکی"),max_length=254)
    content=models.TextField(_("متن پیام"))
    def __str__(self):
        return self.email
    