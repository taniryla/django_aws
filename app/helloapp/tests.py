from django.test import TestCase
from django.urls import reverse
import pytest
from helloapp.models import Helloapp


# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.fixture
def new_helloapp(db):
    helloapp = Helloapp.objects.create(
        title='Helloapp',
        helloapp_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='A lot about Helloapp',
        published=True
    )
    return helloapp

def test_search_helloapps(new_helloapp:
    assert Helloapp.objects.filter(title='Helloapp').exists()

def test_update_helloapp(new_helloapp):
    new_helloapp.title = 'Helloapp'
    new_hello.save()
    assert Helloapp.objects.filter(title='Helloapp').exists()

@pytest.fixture
def another_helloapp(db):
    helloapp = Helloapp.objects.create(
        title='Helloapp',
        helloapp_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Things about Helloapp',
        published=True
    )
    return helloapp

def test_compare_helloapps(new_helloapp, another_helloapp):
    assert new_helloapp.pk != another_helloapp.pk
