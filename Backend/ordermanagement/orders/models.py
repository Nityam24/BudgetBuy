from django.db import models


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, null=True)
    user_id = models.BigIntegerField()
    shipping_address = models.CharField(max_length=200, null=True)
    total_value = models.IntegerField(null=True, default=0)
    payment_method = models.CharField(max_length=50, null=True) 

    class Meta:
        db_table = 'order' 

class Order_item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.BigIntegerField()
    amount = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'order_item'

class Cart(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    total_value = models.IntegerField(null=True, default=0)
    status = models.CharField(max_length=50, null=True, default="available")
    out_of_stock = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = 'cart'


class Cart_item(models.Model):
    product_id = models.BigIntegerField()
    user_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    product_price = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True, default="available")

    class Meta:
        db_table = 'cart_item'


