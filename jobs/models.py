from uuid import uuid4
from django.db import models
from django.utils.timezone import now

# job_types: id, value


class JobType(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    value = models.CharField(max_length=150, null=False)

    class Meta:
        app_label = 'jobs'
        ordering = ('id',)

    def __str__(self):
        return self.value

# jobs: id, title, description, salary_from, salary_to and job_type_id


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=150, null=False)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE, default=0)

    description = models.CharField(max_length=250, default='')
    salary_from = models.FloatField(default=0)
    salary_to = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'jobs'
        ordering = ('updated_at', )

    def __str__(self):
        return self.title
