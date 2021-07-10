from django.db import models


class airport(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class agent(models.Model):
    airport = models.ForeignKey(airport, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    foiz = models.IntegerField(default=0)

    def __str__(self):
        return self.name
