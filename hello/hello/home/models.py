from django.db import models

# Create your models here.
# Register in admin
# In project setting  installed apps add one more by apps in your app name

# makemigrations = create changes and store in a file
# migrate = apply the pending changes created by migrations
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name