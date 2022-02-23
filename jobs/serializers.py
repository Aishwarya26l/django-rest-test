from rest_framework import serializers
from jobs.models import Job, JobType
from core.formators import number_thousand_separator_format, calculate_elapsed_time


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

    def to_representation(self, instance):
        """Use custom formatters"""
        ret = super().to_representation(instance)
        ret['salary_from'] = number_thousand_separator_format(
            ret['salary_from'])
        ret['salary_to'] = number_thousand_separator_format(ret['salary_to'])
        return ret
