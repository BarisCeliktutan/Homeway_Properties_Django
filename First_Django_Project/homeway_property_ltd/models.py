from django.db import models


class Flat(models.Model):
    flat_no = models.CharField(max_length=50)
    building = models.CharField(max_length=300)
    post_code = models.CharField(max_length=50)

    kingsize_beds = models.CharField(max_length=50, default="0")
    double_beds = models.CharField(max_length=50, default="0")
    sofa_beds =  models.CharField(max_length=50, default="0")

    photo_url = models.CharField(max_length=10000, default="")

    def __str__(self):
        return f"{self.flat_no}, {self.building}, {self.post_code}"

class Maintenance_Notes(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    note = models.CharField(max_length=10000)

    done = models.BooleanField(default=False)

    def __str__(self):
        return self.note
    
class Cleaner(models.Model):
    name = models.CharField(max_length=100)                                                                                                         

    def __str__(self):
        return self.name
