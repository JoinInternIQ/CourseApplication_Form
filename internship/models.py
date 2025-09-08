from django.db import models

class InternshipApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]


    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    department = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=50)
    batch_from = models.CharField(max_length=10, null=True, blank=True)  # Course Start Year
    batch_to = models.CharField(max_length=10, null=True, blank=True)    # Graduation Year
    college_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    domains = models.CharField(max_length=100)  # Selected Domain

    

    def __str__(self):
        return self.name

