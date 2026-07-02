from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentCrudTests(TestCase):
    def test_student_list_and_create_flow(self):
        response = self.client.get(reverse('students:student-list'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('students:student-create'), {
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'department': 'Computer Science',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(name='Alice Johnson').exists())
