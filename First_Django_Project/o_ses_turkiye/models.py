from django.db import models


class Yil(models.Model):
    yil = models.CharField(max_length=200)
    
    def __str__(self):
        return self.yil

class Juri(models.Model):
    yil = models.ForeignKey(Yil, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    resim = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
    
class Yarismaci(models.Model):
    juri = models.ForeignKey(Juri, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name