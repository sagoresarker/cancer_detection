from django.db import models
from accounts.models import Account

# Create your models here.
class UploadedContent(models.Model):
    image_id = models.AutoField(primary_key=True, null=False)
    image_name = models.CharField()
    image_tested = models.BooleanField(default=False)
    image_lebel = models.CharField(default=None)
    uploaded_date = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(Account)

    def __str__(self):
        return self.image_name