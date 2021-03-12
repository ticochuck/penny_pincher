from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Result, SearchQuery


class TestRoutes(TestCase):
    """Test Suite for checking routes and templates used
    """

    def test_status_check(self):
        test_data = (
            (reverse('home'), 'ticket_search/home.html'),
            (reverse('about'), 'ticket_search/about.html'),
            # (reverse('search'), 'ticket_search/search.html'),
            #(reverse('results'), 'ticket_search/results.html'),
            (reverse('register'), 'users/register.html'),
            (reverse('login'), 'users/login.html'),
            (reverse('logout'), 'users/logout.html'),
            #(reverse('profile'), 'users/profile.html')
        )

        # Check if each route returns status 200 and uses correct template
        for test in test_data:
            url, template = test[0], test[1]
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, template)


class TestModels(TestCase):
    """Test suite for app models
    """

    def setUp(self):
        """Create test instances of SearchQuery() and Result()
        """

        self.user = get_user_model().objects.create_user(
            username="test",
            email='test@company.com',
            password="test123456")

        self.sq = SearchQuery(
            user=self.user,
            departure_city='Test departure city',
            arrival_city='Test arrival city',
            date_from='2020-01-01',
            date_to='2020-01-02',
            stay_duration=4
        )
        self.sq.save()

        self.result = Result(
            search_query=self.sq,
            departure_city='Test departure city',
            arrival_city='Test arrival city',
            date_from='2020-01-01',
            date_to='2020-01-02',
            price=445.78
        )
        self.result.save()

    def test_search_query(self):
        """Compare saved instance of SearchQuery() with pulled from DB
        """
        record = SearchQuery.objects.get(pk=1)

        self.assertEqual(record, self.sq)

    def test_result(self):
        """Compare saved instance of Result() with pulled from DB
        """
        record = Result.objects.get(pk=1)

        self.assertEqual(record, self.result)
