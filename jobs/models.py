from uuid import uuid4
from django.db import models

# jobs: id, title, description, salary_from, salary_to and job_type_id


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.title
