
from django.db import models

# Create your models here.
from authentication.models import User


class Orders(models.Model):
    SIZES=(
        ('SMALL',"small"),
        ("MEDIUM","medium"),
        ('LARGE',"large"),
        ("EXTRA_LARGE","extra_large")
    )

    ORDER_STATUS=(
        ('ATTENTE',"attente"),
        ("COURS","cours"),
        ("TERMINE","termine")
    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    size=models.CharField(max_length=20,choices=SIZES,default=SIZES[0][0])
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"