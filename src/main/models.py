import uuid
from django.db import models
from users.models import Profile, Location
from .const import CAR_BRANDS, TRANSMISSION_OPTIONS
from .utils import user_listing_path


class listing(models.Model):
 id = models.UUIDField(
  primary_key=True, default=uuid.uuid4, unique=True,editable=False
 )
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
 brand = models.CharField(max_length=24, choices=CAR_BRANDS, default=None)
 model = models.CharField(max_length=74,)
 vin = models.CharField(max_length=17,)
 mileage = models.IntegerField(default=0)
 color = models.CharField(max_length=24)
 description = models.TextField()
 engine = models.CharField(max_length=24)
 transmission = models.CharField(max_length=30, choices=TRANSMISSION_OPTIONS, default=None)
 location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
 image = models.ImageField(upload_to=user_listing_path)


 def __str__(self):
  return f'{self.seller.user.username}\' listing - {self.model}'