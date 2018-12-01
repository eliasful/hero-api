from django.test import TestCase
import unittest
from hero.models import Hero
from rest_framework.test import APIClient

"""
Um herói possuí nome, descrição, uma url para a localização da foto
e uma definição se é ou não favorito
"""
class HeroTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superman = Hero.objects.create(
            name="Superman",
            description="Great superhero",
            favorite=False,
            photo=None,
        )
        self.batman = Hero.objects.create(
            name="Batman",
            description="Lost a parents",
            favorite=False,
            photo="https://vignette.wikia.nocookie.net/batman/images/c/c8/Batman_%2766_-_Adam_West_as_Batman_2.jpg/revision/latest?cb=20140731220401",
        )


    def test_name(self):
        self.assertEquals(self.superman.name, 'Superman')
        self.assertEquals(self.batman.name, 'Batman')
        
        
    def test_get(self):
        response = self.client.get('/heroes/')
        self.assertEquals(response.status_code, 200)


    def test_get_favorites(self):
        response = self.client.get('/heroes/favorites/')
        self.assertEquals(response.status_code, 200)


    def test_get_one(self):
        response = self.client.get('/heroes/1/')
        self.assertEquals(response.status_code, 200)


    def test_post(self):
        response = self.client.post('/heroes/', {
            'name': 'novo herói',
            'description': 'descrição'
        })
        self.assertEquals(response.status_code, 201)


    def test_put(self):
        newName = 'Superman editado'
        response = self.client.put('/heroes/1/', {
            "id": 1,
            "name": newName,
            "description": "Great superhero",
            "photo": None,
            "favorite": False
        })
        editHero = Hero.objects.get(pk=1)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(newName, editHero.name)


    def test_delete(self):
        hero = Hero.objects.create(
            name="Heroi Apagado",
            description="Descrição"
        )
        response = self.client.delete('/heroes/' + str(hero.id) + '/')
        print(response)
        self.assertEquals(response.status_code, 204)
