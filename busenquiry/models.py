from django.db import models

# Create your models here.

class TransportCompany(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}-{}".format(self.name,self.contact)

class Bus(models.Model):
    number = models.CharField(max_length=20)
    capacity = models.IntegerField(default=20)
    model = models.CharField(max_length=20)
    transport_company = models.ForeignKey(TransportCompany,on_delete=models.CASCADE,related_name='bus')
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}-{}".format(self.number,self.model)

class Stops(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "{}".format(self.name)
    
class Routes(models.Model):
    starting_point = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='routes')
    stops = models.ManyToManyField(Stops)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}-{}".format(self.starting_point,self.destination)
    
class Schedule(models.Model):
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    route = models.ForeignKey(Routes,on_delete=models.CASCADE,related_name='schedule_route')
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='schedule_bus')
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.departure_time,self.arrival_time)
    



