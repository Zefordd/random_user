from django.db import models


class RandomUsers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)  # TODO: replace for bool
    location = models.TextField()
    email = models.CharField(max_length=255)
    info = models.TextField()

    class Meta:
        db_table = 'random_users'