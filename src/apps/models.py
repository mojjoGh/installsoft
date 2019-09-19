from django.db import models
from django.urls import reverse

# Create your models here.
class App(models.Model):
    title           = models.CharField(max_length=120) # maxlength is required
    description     = models.TextField(blank=True,null=True)
    category        = models.IntegerField(blank=False, null=False) #models.DecimalField(decimal_places=2,max_digits=10000)
    freatured       = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("app-detail", kwargs={"id": self.id})

    # def get_absolute_url(self):
    #     return f"/apps/{self.id}/"