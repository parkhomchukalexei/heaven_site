from django.db import models
#from users.models import Client,AbstractUser

# Create your models here.


class OnlyFansTable(models.Model):

    date = models.DateField(auto_now=True)
    fp = models.BooleanField(default=False)
    fp_data = models.FloatField(null=True)
    op = models.BooleanField(default=False)
    op_data = models.FloatField(null=True)
    pp = models.BooleanField(default=False)
    pp_data = models.FloatField(null=True)
    client = models.ForeignKey('users.Client', on_delete=models.DO_NOTHING)
    operator = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
