from django.db import models


class pm002(models.Model) :
    fields = '__all__'
    chnnlTypeCd = models.TextField()

    def __str__(self):
        return self.chnnlTypeCd

