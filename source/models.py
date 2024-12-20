from django.db import models

# Create your models here.
class Company(models.Model):

    STATUS_CHOICES = [
        ('','Select'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    SALES_MANAGER_CHOICES = [
        ('', 'Select'),
        ('john_doe', 'John Doe'),
        ('jamie_vardy', 'Jamie Vardy'),
    ]

    TYPE_CHOICES = [
        ('', 'Select'),
        ('customer', 'Customer'),
    ]

    INDUSTRY_CHOICES = [
        ('', 'Select'),
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
    ]

    SIEM_PRODUCT_CHOICES = [
        ('', 'Select'),
        ('trellix_esm', 'Trellix ESM'),
        ('forti_siem', 'Forti SIEM'),
    ]

    company_name = models.CharField(unique=True,max_length=100)
    notified_email_to = models.EmailField()
    notified_email_cc = models.EmailField()
    notified_email_bcc = models.EmailField()
    siem_product = models.CharField(max_length=50, choices=SIEM_PRODUCT_CHOICES,null=True,blank=True)
    siem_username = models.CharField(max_length=100,null=True,blank=True)
    siem_password = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    corporate_sales_manager = models.CharField(max_length=50, choices=SALES_MANAGER_CHOICES )
    authorized_person = models.CharField(max_length=100)
    authorized_person_mobile = models.CharField(max_length=20)
    authorized_person_email = models.EmailField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    industry = models.CharField(max_length=20, choices=INDUSTRY_CHOICES)
    created_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
