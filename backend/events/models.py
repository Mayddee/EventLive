from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import User 

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    EVENT_CATEGORIES = [
        ('CON', 'Concert'),
        ('MOV', 'Movie Premiere'),
        ('THTR', 'Theatre'),
        ('TOUR', 'Tour'),
        ('SHOW', 'Show')
    ]
    category = models.CharField(max_length=4, choices=EVENT_CATEGORIES, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    ticket_cost= models.IntegerField(default=0)
    participants = models.ManyToManyField(User, blank=True)
    date = models.DateTimeField()
    seats = models.IntegerField(default=1)
    available_seats = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Booking(models.Model):
    participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    # event_date = models.DateTimeField()
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.participant} has registered for {self.event}'
    




# class Actor(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)

# class Concert(Event):
#     duration = models.TextField(null=True, blank=True)
#     # actors = models.ManyToManyField(Actor)
#     # date = models.DateField()

# class Movie(Event):
#     country = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     actors = models.ManyToManyField(Actor)
#     # start_date = models.DateField()
#     # end_date = models.DateField()

# class Theatre(Event):
#     actors = models.ManyToManyField(Actor)
#     # date = models.DateField()

# class Category(models.Model):
#     name = models.CharField(max_length=100)
 
# class Event(models.Model):
#     EVENT_CATEGORIES = [
#         ('CON', 'Concert'),
#         ('MOV', 'Movie Premiere'),
#         ('THTR', 'Theatre'),
#         ('TOUR', 'Tour'),
#         ('SHOW', 'Show')
#     ]
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=4, choices=EVENT_CATEGORIES)

#     # category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     priority = models.IntegerField(default=1)
#     description = models.TextField(default='')
#     location = models.CharField(max_length=255, default='')
#     organizer = models.CharField(max_length=100, default='')

#     def __str__(self):
#         return f'{self.name}, {self.category}, {self.start_date} - {self.end_date}, {self.location}'
    

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     event_date = models.DateTimeField()
    

#     def __str__(self):
#         return f'{self.user} has registered to {self.event} that will be hold on {self.event_date}'
        