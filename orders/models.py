
from django.db import models, transaction

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
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="order")
    size=models.CharField(max_length=20,choices=SIZES,default=SIZES[0][0])
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    quantity=models.IntegerField()
    active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @transaction.atomic
    def modify_activation(self):
        self.active=not self.active
        self.save()


    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"