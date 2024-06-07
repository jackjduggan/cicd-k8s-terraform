from django.test import TestCase
from .models import Project
from django.utils import timezone

class ProjectModelTest(TestCase):

    def setUp(self):
        Project.objects.create(
            name="Test Project", 
            description="An Awesome Project",
            start_date=timezone.now().date()
            )

    def test_project_creation(self):
        project = Project.objects.get(name="Test Project")
        self.assertEqual(project.description, "An Awesome Project")
