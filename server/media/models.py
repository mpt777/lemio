import datetime
import uuid
from django.db import models

# Create your models here.

def handle_uploaded_file(instance, filename):
    # _datetime = datetime.datetime.now()
    # datetime_str = _datetime.strftime("%Y-%m-%d-%H-%M-%S")
    # return f"private/{datetime_str}-{filename}"
    return f"private/{str(uuid.uuid4())}"

def public_handle_uploaded_file(instance, filename):
    # _datetime = datetime.datetime.now()
    # datetime_str = _datetime.strftime("%Y-%m-%d-%H-%M-%S")
    # return f"public/{datetime_str}-{filename}"
    return f"private/{str(uuid.uuid4())}"


class Post(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to=handle_uploaded_file, blank=True, null=True)
    public_file = models.FileField(upload_to=public_handle_uploaded_file, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    
    

