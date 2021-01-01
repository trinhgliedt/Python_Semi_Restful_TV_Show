from django.db import models
from datetime import datetime
from time import strftime, strptime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, post_data, method):
        errors = {}

        if len(post_data["network"]) < 3:
            errors["network"] = "Please enter a network of at least 3 characters."
        if len(post_data["released_date"]) == 0:
            errors["released_date"] = "Please enter a released date."
        elif datetime.strptime(post_data['released_date'], "%Y-%m-%d").date() > datetime.now().date():
            errors["released_date"] = "Please enter a released date that is before today."
        if 1<= len(post_data["desc"]) < 10:   
            errors["description"] = "Please enter a description of at least 10 characters."
        if method == "Add":
            errorsAdd = errors
            if len(post_data["tittle"]) < 2:
                errorsAdd["tittle"] = "Please enter a title of at least 2 characters"
            elif Show.objects.filter(tittle = post_data["tittle"]).exists():
                errorsAdd["tittle"] = "A show with the same tittle is already in the list. Please enter another show."
            return errorsAdd
        if method == "Edit":
            errorsEdit = errors
            if len(post_data["tittle"]) < 2:
                errorsEdit["tittle"] = "Please enter a title of at least 2 characters"
            return errorsEdit


class Show(models.Model):
    tittle = models.CharField(max_length=255)
    network = models.CharField(max_length=60)
    released_date = models.DateTimeField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ShowManager()
