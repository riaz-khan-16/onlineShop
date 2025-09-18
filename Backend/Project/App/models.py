from django.db import models

class Shop(models.Model):
    name=models.CharField(max_length=200, default="AmarDokan", null=True, blank=True)
    type=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class WebContent(models.Model):
    shop=models.OneToOneField(Shop, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
  
class Category(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Product(models.Model):
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200)
    short_description=models.CharField(max_length=400, null=True, blank=True)
    how_to_use=models.CharField(max_length=1000, null=True, blank=True)
    see_demo_video=models.CharField(max_length=200, null=True, blank=True)
    payment_type=models.CharField(max_length=200, null=True, blank=True)
    image1 = models.ImageField(upload_to='products/', null=True, blank=True) 
    image_description1=models.CharField(max_length=200, null=True, blank=True)
    image2 = models.ImageField(upload_to='products/', null=True, blank=True) 
    image_description2=models.CharField(max_length=200, null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True) 
    image_description3=models.CharField(max_length=200, null=True, blank=True)
    youtube_video_link=models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return str(self.id)+'. '+ self.name
    

    
