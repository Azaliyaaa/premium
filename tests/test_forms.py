from django.test import SimpleTestCase
from taskmanager.forms import CreateUserForm, TaskForm

from django.forms import TextInput
from django.contrib.auth.models import User

class TestForms(SimpleTestCase):
    def test_CreateUserForm(self):
        response = self.client.post("/my/form", {'something':'something'})
        self.assertEqual(response.status_code, 200)

class TestForm(SimpleTestCase):
    form = CreateUserForm(data={})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def test_TaskForm(self):
        form = TaskForm(data={})

        class Meta:
            model = Task
            fields = ['title','task']
            widgets = {'title' : TextInput(attrs={
                'class' : 'form-control',
                'title' : 'task',
                 })}

