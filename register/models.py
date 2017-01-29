# for later: from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django_pandas.managers import DataFrameManager


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.category_name

class Entry(models.Model):
    CURR = (
        ('PHP', 'Phil. Peso'),
        ('THB', 'Thai Baht'),
        ('EUR', 'Euro'),
        ('USD', 'Dollar'),
        ('CHF', 'Franken'),
    )

    #for later: user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    date = models.DateField()
    category = models.ForeignKey('Category')
    amount = models.FloatField()
    currency = models.CharField(max_length=3,choices=CURR, default="PHP")
    curr_out = models.CharField(max_length=3,choices=CURR, default="CHF")
    comments = models.CharField(max_length=50, null=True, blank=True)
    amount_out = models.FloatField(null=True, blank=True)
    curr_out = models.CharField(max_length=3,choices=CURR, default="CHF")

    objects = DataFrameManager()

    def __str__(self):
        return ("%s %s for %s on %s") %(self.amount, self.currency, self.category, self.date)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {"pk": self.pk})
