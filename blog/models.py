from django.db import models

# Create A Blog models
# Add the Blog app to the settings
# Create a migration
# Migrate
# Add to the admin

class Blog(models.Model):

    title = models.CharField(max_length = 255, default = 'No title')
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')
#    summary = models.CharField(max_length = 200)
