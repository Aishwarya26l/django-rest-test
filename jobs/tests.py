import json
from uuid import uuid4
from django.urls import reverse
from rest_framework.test import APITestCase
from jobs.models import Job, JobType
from rest_framework import status

base_path = "api/v1/"


class JobTypesTests(APITestCase):
    fixtures = ['seed.json']

    def test_job_types_seed(self):
        """
        Ensure jobtype table is seeded with values
        """
        response = self.client.get(reverse('jobType_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(JobType.objects.count(), 0)


class JobTests(APITestCase):
    fixtures = ['seed.json']

    def setUp(self):
        # Jobs to be modified
        self.first_job = Job.objects.create(
            title="Dummy 1", job_type=JobType.objects.get(id=1))
        self.second_job = Job.objects.create(
            title="Dummy 2", job_type=JobType.objects.get(id=2))

        self.valid_job = {
            "title": "valid data",
            "job_type": "Full time"
        }
        self.invalid_job_title = {
            "title": "",
            "job_type": "Full time"
        }
        self.invalid_job_type = {
            "title": "Invalid Job type",
            "job_type": "All the time"
        }

    def test_job_str(self):
        self.assertEqual(str(self.first_job), "Dummy 1")

    def test_job_type_str(self):
        self.assertEqual(str(JobType.objects.get(id=2)), "Part time")

    def test_create_job(self):
        """
        Ensure we create a new job object.
        """
        response = self.client.post(reverse('job_list'),
                                    json.dumps(self.valid_job),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_job_invalid_job_type(self):
        """
        Ensure invalid job type fails job creation.
        """
        response = self.client.post(reverse('job_list'),
                                    json.dumps(self.invalid_job_type),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_job_empty_title(self):
        """
        Ensure empty title fails job creation.
        """
        response = self.client.post(reverse('job_list'),
                                    json.dumps(self.invalid_job_title),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_job_empty_job_type(self):
        """
        Ensure empty job_type fails job creation.
        """
        data = {
            "title": "Dummy"
        }
        response = self.client.post(reverse('job_list'),
                                    json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_jobs(self):
        """
        Ensure we can fetch jobs
        """
        response = self.client.get(reverse('job_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.count(), 2)

    def test_retrieve_job_by_id(self):
        """
        Ensure we can retrieve job by id
        """
        checkId = self.first_job.pk

        response = self.client.get(
            reverse('job_detail', kwargs={'pk': checkId}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['id'], str(checkId))

    def test_retrieve_job_by_nonexistent_id(self):
        """
        Ensure we can't retrieve job by non existent id
        """
        checkId = uuid4()  # random uuid
        response = self.client.get(
            reverse('job_detail', kwargs={'pk': checkId}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_job(self):
        '''
        Ensure job with a given id is updated
        '''
        updated_data = {
            "title": "Updated Dummy",
            "job_type": "Part time"
        }
        checkId = self.first_job.pk

        response = self.client.put(
            reverse('job_detail', kwargs={'pk': checkId}),
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['title'], "Updated Dummy")

    def test_invalid_update_job(self):
        '''
        Ensure job with a invalid id is not updated
        '''
        updated_data = {
            "title": "Updated Dummy",
            "job_type": "Part time"
        }
        checkId = uuid4()

        response = self.client.put(
            reverse('job_detail', kwargs={'pk': checkId}),
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_input_update_job(self):
        '''
        Ensure job with a invalid id is not updated
        '''
        updated_data = {
            "title": "Updated Dummy"
        }
        checkId = self.first_job.pk

        response = self.client.put(
            reverse('job_detail', kwargs={'pk': checkId}),
            data=json.dumps(updated_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_job(self):
        '''
        Ensure job with a given id is deleted
        '''
        checkId = self.first_job.pk

        response = self.client.delete(
            reverse('job_detail', kwargs={'pk': checkId}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_job(self):
        '''
        Ensure job with a invalid id is not deleted
        '''
        checkId = uuid4()

        response = self.client.delete(
            reverse('job_detail', kwargs={'pk': checkId}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
