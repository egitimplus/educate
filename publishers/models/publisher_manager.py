from django.db import models


class PublisherManager(models.Model):
    manager = models.ForeignKey('users.User', on_delete=models.CASCADE)
    publisher = models.ForeignKey('publishers.Publisher', on_delete=models.CASCADE)

    class Meta:
        db_table = 'publishers_publisher_manager'
