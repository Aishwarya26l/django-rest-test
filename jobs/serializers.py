from rest_framework import serializers
from jobs.models import Job, JobType
from core.formators import number_thousand_separator_format, calculate_elapsed_time
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ('id',
                  'value')


class JobSerializer(serializers.ModelSerializer):
    # Add job_type reference for each job
    job_type = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='value',
        queryset=JobType.objects.all()
    )

    class Meta:
        model = Job
        fields = ('id',
                  'title',
                  'job_type',
                  'description',
                  'salary_from',
                  'salary_to',
                  'created_at',
                  'updated_at')

    def elapsed_time(self, time):
        diff = (now() - parse_datetime(time)).seconds
        if diff == 0:
            return 'Now'
        else:
            return calculate_elapsed_time(diff)

    def to_representation(self, instance):
        """Use custom formatters"""
        ret = super().to_representation(instance)
        ret['salary_from'] = number_thousand_separator_format(
            ret['salary_from'])
        ret['salary_to'] = number_thousand_separator_format(ret['salary_to'])
        ret['created_at'] = self.elapsed_time(ret['created_at'])
        ret['updated_at'] = self.elapsed_time(ret['updated_at'])
        return ret
