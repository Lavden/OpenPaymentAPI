from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    user_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=5, blank=True)
    user_type = models.CharField(max_length=20, blank=True)

    # def __str__(self):
    #     return self.user_id

class Record(models.Model):
    recipient_id = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    sender_id = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    record_id = models.CharField(max_length=10, blank=False,primary_key=True)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)

