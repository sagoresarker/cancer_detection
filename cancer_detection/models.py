from django.db import models
from accounts.models import User

LEBEL = (
    ('Tested', 'Tested'),
    ('Not Tested', 'Not Tested'),
)

# Create your models here.
class UploadedContent(models.Model):
    image_id = models.AutoField(primary_key=True, null=False)
    image_name = models.CharField(max_length=250)
    image_tested = models.BooleanField(default=False)
    image_lebel = models.CharField(choices=LEBEL, default='Not Tested', max_length=100)
    uploaded_date = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name