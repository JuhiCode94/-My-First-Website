from django.db import models

# Create your models here.
class Contact(models.Model):
    # Field to store the name of the contact
    name = models.CharField(max_length=100)
    # Field to store the email of the contact
    email = models.EmailField()
    # Field to store the message from the contact
    message = models.TextField()
    # Field to store the timestamp of when the contact was created
    timestamp = models.DateTimeField(auto_now_add=True)

    # Method to return a string representation of the Contact object
    def __str__(self):
        # Returns the name and email of the contact
        return f"{self.name} ({self.email})"

 # Model to store order information   
class Order(models.Model):
    # Field to store the name of the item ordered
    item = models.CharField(max_length=100)
    # Field to store the price of the item ordered
    price = models.FloatField()
    # Field to store the quantity of the item ordered
    quantity = models.IntegerField()
    # Field to store the total price for the order
    total_price = models.FloatField()
    # Field to store the name of the person who placed the order
    name = models.CharField(max_length=100)
    # Field to store the email of the person who placed the order
    email = models.EmailField()
    # Field to store the phone number of the person who placed the order
    phone = models.CharField(max_length=20)
    # Field to store the street address for the order delivery
    street = models.CharField(max_length=200)
    # Field to store the city for the order delivery
    city = models.CharField(max_length=100)
    # Field to store the state for the order delivery
    state = models.CharField(max_length=100)
    # Field to store the postal code for the order delivery
    postal_code = models.CharField(max_length=20)
    # Field to store the country for the order delivery
    country = models.CharField(max_length=100)
    # Field to store the timestamp of when the order was placed
    timestamp = models.DateTimeField(auto_now_add=True)

    # Method to return a string representation of the Order object
    def __str__(self):
        # Returns the order ID, item, and name of the person who placed the order
        return f"Order {self.id} - {self.item} - {self.name}"   

# Model to store subscriber information   
class Subscriber(models.Model):
    # Field to store the email of the subscriber
    email = models.EmailField(unique=True)
    # Field to store the timestamp of when the subscription was created
    timestamp = models.DateTimeField(auto_now_add=True)

    # Method to return a string representation of the Subscriber objec
    def __str__(self):
        # Returns the email of the subscriber
        return self.email   