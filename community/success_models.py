from django.db import models

class SuccessStory(models.Model):
    beneficiary_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='success_stories/')
    testimonial = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.beneficiary_name
