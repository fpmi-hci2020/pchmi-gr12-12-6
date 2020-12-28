from django.db import models

class Tickets(models.Model):
    From = models.CharField('Откуда', max_length=16)
    Where = models.CharField('Куда', max_length=16)
    Date = models.DateField('Дата', max_length=10)
    Carrier = models.CharField('Перевозчик', max_length=10)
    Price = models.DecimalField('Цена', max_digits=7, decimal_places=2)


    def __str__(self):
        return self.From.__str__() + ' ' + self.Where.__str__() + ' ' + self.Date.__str__() + ' ' + self.Carrier.__str__() + ' ' + self.Price.__str__()
