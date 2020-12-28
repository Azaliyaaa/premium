from django.test import TestCase
from unittest import TestCase
from test.models import Task

class TestTask(TestCase):

    def setUp(self):
        self.Task1 = Task.objects.create(
            name = 'Task1'

        )

    def test__str__(self):
          return self.Product1