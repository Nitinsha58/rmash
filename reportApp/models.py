from django.db import models
from users.models import CustomUser

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="report")
    report_id = models.CharField(max_length=255, unique=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    report_data = models.TextField()