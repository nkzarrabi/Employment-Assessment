#tests/test_views.py

import pytest
from django.urls import reverse
from django.test import Client
#from role_customization.models import Role

@pytest.mark.django_db
def test_hr_dashboard():
    client = Client()
    response = client.get(reverse('hr_dashboard'))
    assert response.status_code == 200
    assert 'hr_dashboard/index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_role_list():
    client = Client()
    response = client.get(reverse('role_list'))
    assert response.status_code == 200
    assert 'role_customization/role_list.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_role_create_get():
    client = Client()
    response = client.get(reverse('role_create'))
    assert response.status_code == 200
    assert 'role_customization/role_form.html' in [t.name for t in response.templates]

'''
@pytest.mark.django_db
def test_role_create_post():
    client = Client()
    response = client.post(reverse('role_create'), {'name': 'Test Role'})
    assert response.status_code == 302  # Redirect after successful creation
    assert Role.objects.filter(name='Test Role').exists()

@pytest.mark.django_db
def test_role_update_get():
    role = Role.objects.create(name='Test Role')
    client = Client()
    response = client.get(reverse('role_update', args=[role.pk]))
    assert response.status_code == 200
    assert 'role_customization/role_form.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_role_update_post():
    role = Role.objects.create(name='Test Role')
    client = Client()
    response = client.post(reverse('role_update', args=[role.pk]), {'name': 'Updated Role'})
    assert response.status_code == 302  # Redirect after successful update
    role.refresh_from_db()
    assert role.name == 'Updated Role'
'''
    