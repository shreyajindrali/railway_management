from django.db import models

class Train(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.source} to {self.destination}"

class Booking(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    seats_booked = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.train}"

