from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Sujeto(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    title = models.CharField(max_length=200)
    datos = models.TextField()
    datos1 = models.CharField(max_length=200, null=True, blank=True)
    sig = models.ImageField(upload_to='graf/', null=True, blank=True )
    rmtc = models.TextField(null=True, blank=True)
    fr1 = models.TextField(null=True, blank=True)
    fr2 = models.TextField(null=True, blank=True)
    fr3 = models.TextField(null=True, blank=True)
    fr4 = models.TextField(null=True, blank=True)
    fr5 = models.TextField(null=True, blank=True)
    his = models.ImageField(upload_to='graf/', null=True, blank=True)
    fa1 = models.TextField(null=True, blank=True)
    fa2 = models.TextField(null=True, blank=True)
    fa3 = models.TextField(null=True, blank=True)
    gra = models.ImageField(upload_to='graf/', null=True, blank=True)
    fs1 = models.TextField(null=True, blank=True)
    fs3 = models.TextField(null=True, blank=True)
    grs = models.ImageField(upload_to='graf/', null=True, blank=True)
    comp1 = models.TextField(null=True, blank=True)
    comp2 = models.TextField(null=True, blank=True)
    comp3 = models.TextField(null=True, blank=True)
    grp = models.ImageField(upload_to='graf/', null=True, blank=True)
    fp = models.TextField(null=True, blank=True)
    comp4 = models.TextField(null=True, blank=True)
    comp5 = models.TextField(null=True, blank=True)
    comp6 = models.TextField(null=True, blank=True)
    comp7 = models.TextField(null=True, blank=True)
    comp8 = models.TextField(null=True, blank=True)
    comp9 = models.TextField(null=True, blank=True)
    grp1 = models.ImageField(upload_to='graf/', null=True, blank=True)
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
                blank=True, null=True)

    def __str__(self):
        return self.title

class Comparacion(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    tit = models.CharField(max_length=200)
    dat = models.TextField()
    dat1 = models.TextField(max_length=200, null=True, blank=True)
    comp = models.ImageField(upload_to='graf/', null=True, blank=True )

    def __str__(self):
        return self.tit

# Create your models here.
