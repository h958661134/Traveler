from django.db import models

# Create your models here.

# class Liaa(models.Model):
#     id = models.IntegerField(primary_key=True)
#     liaaname = models.CharField(max_length=100, blank=True, null=True)
#     litext = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'liaa'


class Li(models.Model):
    liname = models.CharField(max_length=255, blank=True, null=True)
    litext = models.TextField(blank=True, null=True)
    lipicture = models.TextField(blank=True, null=True)
    # id = models.IntegerField(primary_key=True)
    sign = models.IntegerField(blank=True, null=True)
    one = models.CharField(max_length=255, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'li'

class forum(models.Model):
    Postname=models.CharField(max_length=255, blank=True, null=True)
    Content=models.TextField(blank=True, null=True)
    Id = models.IntegerField(primary_key=True)
    sign = models.IntegerField(blank=True, null=True)
    class Meta:
        permissions = (
            ("add_delete_alter", "Can add/delete/alter the aticle"),
        )
        # managed=False
        # db_table='forum'