from django.core.urlresolvers import reverse
from django.test.client import Client
from django.utils import unittest, simplejson


class CustomerTestCase(unittest.TestCase):
    def test_customer_crud(self):
        c = Client()

        customer = {'name': 'My First Customer'}

        response = c.post(reverse('customer:api:customers:list'), customer)
        self.assertEqual(201, response.status_code)  # HTTP Created
        self.assertIn('Location', response)
        location = response['Location']

        response = c.get(location)
        self.assertEqual(200, response.status_code)  # HTTP OK

        content = simplejson.loads(response.content)
        self.assertEqual(customer['name'], content['name'])
        self.assertEqual(location, content['url'])
        self.assertIn('phone_numbers', content)

        customer['name'] = 'John Doe'
        response = c.put(location, customer)
        self.assertEqual(200, response.status_code)  # HTTP OK
        content = simplejson.loads(response.content)
        self.assertEqual(customer['name'], content['name'])
        self.assertEqual(location, content['url'])
        self.assertIn('phone_numbers', content)

        response = c.delete(location)
        self.assertEqual(204, response.status_code)  # HTTP No Content

        response = c.get(location)
        self.assertEqual(404, response.status_code)  # HTTP Not Found
