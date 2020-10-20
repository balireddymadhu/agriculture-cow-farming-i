from django.db import models


class College(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "College"



class Emp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Emp"
