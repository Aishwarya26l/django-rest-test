# django-rest-technical-test

This test is created based on the Django Rest Framework https://www.django-rest-framework.org/

# Goal
Create restful API endpoints

4 restful API endpoints are required
- Get job detail
- Create job
- Update job
- Delete job

# Instructions
1. Only need to update the files under `jobs` directory
2. Copy `.env-local.example` file into your own `.env` file
3. Two tables are needed to create with model migrations: `jobs` and `job_types` 


# Tables information
- jobs: id, title, description, salary_from, salary_to and job_type_id 
- job_types: id, value
- Seed record for `job_types` table: Full time, Part time, and Freelance