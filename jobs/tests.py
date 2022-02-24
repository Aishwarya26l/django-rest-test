import json
from django.urls import reverse
from rest_framework.test import APITestCase
from jobs.models import Job, JobType
from rest_framework import status

base_path = "api/v1/"


class JobTests(APITestCase):
    fixtures = ['seed.json']

    def helper_create_job(self, data):
        url = reverse('job_list')
        response = self.client.post(url,
                                    json.dumps(data),
                                    content_type='application/json')
        return response

    def test_job_types_seed(self):
        """
        Ensure jobtype table is seeded with values
        """
        url = reverse('jobType_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(JobType.objects.count(), 0)

    def test_create_job(self):
        """
        Ensure we create a new job object.
        """
        url = reverse('job_list')
        data = {
            "title": "Demo",
            "description": "This is a test",
            "salary_to": 1000000,
            "salary_from": 10000,
            "job_type": "FULL TIME"
        }
        response = self.client.post(url,
                                    json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 1)
        self.assertEqual(Job.objects.get().title, "Demo")

    def test_create_job_invalid_job_type(self):
        """
        Ensure invalid job type fails job creation.
        """
        url = reverse('job_list')
        data = {
            "title": "Test 2",
            "job_type": "Random type"
        }
        response = self.client.post(url,
                                    json.dumps(data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['data']['job_type'],
                         ["Object with value=Random type does not exist."])

    def test_create_job_empty_title(self):
        """
        Ensure empty title fails job creation.
        """
        url = reverse('job_list')
        data = {
            "job_type": "Full time"
        }
        response = self.client.post(url,
                                    json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['data']['title'],
                         ["This field is required."])

    def test_create_job_empty_job_type(self):
        """
        Ensure empty job_type fails job creation.
        """
        url = reverse('job_list')
        data = {
            "title": "Dummy"
        }
        response = self.client.post(url,
                                    json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['data']['job_type'],
                         ["This field is required."])

    def test_retrieve_job(self):
        """
        Ensure we create a new job object and can fetch job
        """
        data = {
            "title": "Get job check",
            "job_type": "Full time"
        }
        response = self.helper_create_job(data)

        url = reverse('job_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.count(), 1)
        self.assertEqual(Job.objects.get().title, "Get job check")

    def test_retrieve_jobs(self):
        """
        Ensure we create a new job objects and can fetch jobs
        """
        for _ in range(5):
            data = {
                "title": "Get job check",
                "job_type": "Full time"
            }
            response = self.helper_create_job(data)

        url = reverse('job_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.count(), 5)
