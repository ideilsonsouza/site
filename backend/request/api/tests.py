from django.test import Client, TestCase


class APITestCase(TestCase):

    def setUp(self):

        self.client = Client()


    def test_api_status_200(self):

        response = self.client.get("/api/test/")

        self.assertEqual(response.status_code, 200)
