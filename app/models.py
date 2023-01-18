from django.db import models

from travelreviewwebsite import settings


class Item(models.Model):
    TYPE_CHOICES = (
        ('HOTEL', "Hotel"),
        ('TOURIST_ATTRACTION', "Tourist Attraction"),
        ("CONCERT", "Concert"),
        ("AMUSEMENT_PARK", "Amusement Park"),
    )

    LOCATION_CHOICES = (
        ("DXB", "Dubai"),
        ("AD", "Abu Dhabi"),
        ("RAK", "Ras Al Khaimah"),
        ("SHJ", "Sharjah"),
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    photo = models.ImageField(upload_to="gallery")
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, )
    reviewed_by = models.CharField(max_length=50)
    reviewed_by_email = models.EmailField()
    review = models.TextField()
    reviewed_on = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.review

    def item_detail(self):
        return self.item
