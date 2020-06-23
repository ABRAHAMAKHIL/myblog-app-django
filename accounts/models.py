from django.db import models


STATUS=(

(0,"DRAFT"),
(1,"PUBLISH")

)

class Post(models.Model):
    Title = models.CharField(max_length=200,unique=True)
    Key = models.SlugField(max_length=200,unique=True)
    Writer = models.CharField(max_length=200)
    model_pic = models.ImageField(null=True,blank=True) 
    
    Updated_On = models.DateTimeField(auto_now=True)
    
    Content = models.TextField()
    Created_On = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(choices=STATUS,default=0)
    class Meta:
        ordering = ['-Created_On']
    def __str__(self):
        return self.Title








    

