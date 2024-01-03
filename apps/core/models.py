from django.db import models
import uuid
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class FileModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    title = models.CharField(max_length=250, blank=True)
    path = models.FileField("files", upload_to='data/files/', blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "File"

class BaseModel(models.Model):
    def save(self, *args, full_clean=True, **kwargs):
        if full_clean:
            self.full_clean()
            super().save(*args, **kwargs)

    class Meta(object):
        abstract = True

class Profiles(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.PROTECT,
        verbose_name="Related user", help_text="User linked to this profile")

    firstname = models.CharField(verbose_name="firstname",blank=True, null=True, max_length=256)
    lastname = models.CharField(verbose_name="lastname",blank=True, null=True, max_length=256)
    email = models.EmailField(verbose_name='email', default='', max_length=250, blank=True)
    contact = models.CharField(verbose_name='contact', default='', max_length=250, blank=True)
    live_user = (
        (0, 'Faol emas'),
        (1, 'Faol'),
    )
    live = models.IntegerField(default=1, choices=live_user)
    class Meta(object):
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        try:
            return self.lastname +' '+ self.firstname
        except Exception as er:
            return self.user