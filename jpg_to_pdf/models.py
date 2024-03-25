from django.db import models


# Create your models here.
class JpgToPdf(models.Model):
    jpg_file = models.ImageField(upload_to='jpg_conversions')
    pdf_file = models.FileField(upload_to='pdf_conversions')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jpg_file.name} to {self.pdf_file.name}"