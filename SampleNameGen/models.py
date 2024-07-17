from django.db import models
from django.utils import timezone

class Sample(models.Model):
    sample_id = models.TextField(primary_key=True)
    project_name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    storage_type = models.CharField(max_length=100)
    tissue_type = models.CharField(max_length=100)
    sample_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    replicate = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.project_name}_{self.institution}_{self.technology}_{self.storage_type}_{self.sample_name}_{self.origin}_{self.condition}_{self.replicate}"
