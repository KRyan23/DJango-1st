from django.db import models

# Create your models here.

class Item(models.Model): 
    # ^ this inherits the models class so it can be used
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

#Overides the default inherited class that wou;d notmally display the oject id and 
#instead returns the name of our created item we added in the admin panel.

    def __str__(self):
        return self.name