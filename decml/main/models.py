from django.db import models


class Emails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True,)


    def __str__(self):
        return f"Contact form completion from {self.first_name} - {self.email}"