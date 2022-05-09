from django.db import models


# Create your models here.
class Income(models.Model):
    sum = models.IntegerField(null=False, verbose_name='Income summary')
    created_at = models.DateField(null=False, auto_now_add=True)
    
    def __str__(self):
        return f'Income from {self.created_at}'
    
    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
        ordering = ['-created_at']


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Outcome(models.Model):
    sum = models.IntegerField(null=False)
    created_at = models.DateField(null=False, auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Outcome for {self.category_id}'
    
    class Meta:
        verbose_name = 'Outcome'
        verbose_name_plural = 'Outcomes'
        ordering = ['-created_at']
