from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"""
            ID:{self.id}
            {self.title} 
            ({self.rating}), written by {self.author}, which is best-selling: {self.is_best_selling} 
            """

    