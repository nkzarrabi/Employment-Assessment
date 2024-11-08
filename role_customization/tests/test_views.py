from django.test import TestCase
from django.urls import reverse
from role_customization.models import Role

class ViewsTestCase(TestCase):
    def test_hr_dashboard(self):
        response = self.client.get(reverse('hr_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hr_dashboard/index.html')

    def test_role_list(self):
        response = self.client.get(reverse('role_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'role_customization/role_list.html')

    def test_role_create_get(self):
        response = self.client.get(reverse('role_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'role_customization/role_form.html')

    def test_role_create_post(self):
        response = self.client.post(reverse('role_create'), {'name': 'Test Role', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Role.objects.filter(name='Test Role').exists())
