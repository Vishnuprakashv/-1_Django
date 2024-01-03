from django.db import models

# Create your models here.

class Book_store(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    pieces = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()

    def update_book(self, new_pieces, new_price):
# Update pieces and price
        self.pieces += new_pieces
        self.price = new_price
# Recalculate total
        self.total = self.pieces * self.price
# Save the changes
        self.save()


    



