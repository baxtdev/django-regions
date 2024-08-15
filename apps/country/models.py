from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название страны')
    alpha2_code = models.CharField(max_length=2, unique=True)
    alpha3_code = models.CharField(max_length=3, unique=True)
    
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ['name']  

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название регона")
    country = models.ForeignKey(Country, related_name='regions', on_delete=models.CASCADE,verbose_name="Страна")

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
        ordering = ['name']  

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class City(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название города")
    region = models.ForeignKey(Region, related_name='cities', on_delete=models.CASCADE,verbose_name="Регион")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ['name']  

    def __str__(self):
        return f"{self.name}, {self.region.name}, {self.region.country.name}"
