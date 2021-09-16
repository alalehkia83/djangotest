from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title=models.CharField(_("عنوان"),max_length=50)
    description= models.CharField(_("توضیحات"),max_length=100)
    content= models.TextField(_("متن"))
    created_at=models.DateField(_("زمان انتشار"),default= timezone.now)
    author=models.ForeignKey(User,verbose_name=_("نویسنده"),on_delete=models.CASCADE )
    image= models.ImageField(_("تصویر"),upload_to= "blog/",blank=True,null=True)
    category=models.ForeignKey("Category",related_name="blog",verbose_name=_("دسته بندی"),on_delete=models.CASCADE , blank=True,null=True)
    tags=models.ManyToManyField("tag",verbose_name=_("تگ ها"),related_name="blogs",blank=True,null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(_("عنوان"),max_length=50)
    slug=models.SlugField(_("عنوان لاتین"))
    published_at=models.DateField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(_("عنوان"),max_length=50)
    slug=models.SlugField(_("عنوان لاتین"))
    published_at=models.DateField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    updated_at=models.DateField(_("تاریخ انتشار"),auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.title
class Comments(models.Model):
    blog=models.ForeignKey("Blog",verbose_name=_("مقاله"),related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(_("نام کاربر"),max_length=100)
    email=models.EmailField(_("آدرس الکترونیکی"),max_length=254)
    message=models.TextField(_("متن پیام"))
    date=models.DateField(_("تاریخ نشر"),auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.email



