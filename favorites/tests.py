from django.http import response
from django.test import TestCase
from django.utils.encoding import uri_to_iri
import rest_framework
from .models import Movie
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class MovieModeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='hisham',
            password='password'
        )
        test_user.save()

        test_movie = Movie.objects.create(
            name='fight club',
            rate=5.0,
            publish=1999,
            genre='action',
            description='good movie',
            admin=test_user
        )
        test_movie.save()

    def test_movie_content(self):
        movie = Movie.objects.get(id=1)
        self.assertEqual(movie.name,'fight club')
        self.assertEqual(movie.rate,5.0)
        self.assertEqual(movie.publish,1999)
        self.assertEqual(movie.genre,'action')
        self.assertEqual(movie.description,'good movie')
        self.assertEqual(str(movie.admin),'hisham')

class API_test(APITestCase):
    
    def test_lest(self):
        url = reverse('favorite_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_detail(self):
        user = get_user_model().objects.create_user(
            username='hisham',
            password='password'
        )
        user.save()

        movie = Movie.objects.create(
            name='fight club',
            rate=5.0,
            publish=1999,
            genre='action',
            description='good movie',
            admin=user
        )
        movie.save()
        url = reverse('favorite_detail',args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'name':movie.name,
            'rate':movie.rate,
            'publish':movie.publish,
            'genre':movie.genre,
            'description':movie.description,
            'admin':movie.admin.id
        })

    def test_create(self):
        url = reverse('favorite_list')
        user = get_user_model().objects.create_user(
            username='hisham',
            password='password'
        )
        user.save()
        data = {
            'id':1,
            'name':'hamlet',
            'rate':1,
            'publish':1990,
            'genre':'drama',
            'description':'based on hamlet play',
            'admin':user.id
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,user.id)
        self.assertEqual(Movie.objects.count(),1)
        self.assertEqual(Movie.objects.get().name,data['name'])

    def test_update(self): 
        user = get_user_model().objects.create_user(
            username='hisham',
            password='password'
        )
        user.save()

        movie = Movie.objects.create(
            name='fight club',
            rate=5.0,
            publish=1999,
            genre='action',
            description='good movie',
            admin=user
        )
        movie.save()
        url = reverse('favorite_detail',args=[movie.id])
        data = {
            'id':1,
            'name':'hamlet',
            'rate':1,
            'publish':1990,
            'genre':'drama',
            'description':'based on hamlet play',
            'admin':user.id
        }
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK,url)
        self.assertEqual(Movie.objects.count(),movie.id)
        self.assertEqual(Movie.objects.get().genre,data['genre'])

    def test_delete(self):
        user = get_user_model().objects.create_user(
            username='hisham',
            password='password'
        )
        user.save()

        movie = Movie.objects.create(
            name='fight club',
            rate=5.0,
            publish=1999,
            genre='action',
            description='good movie',
            admin=user
        )
        movie.save()
        url = reverse('favorite_detail',kwargs={'pk':movie.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT,url)