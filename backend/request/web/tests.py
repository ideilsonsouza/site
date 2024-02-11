from django.test import Client, TestCase


class PageAccessTestCase(TestCase):

    def setUp(self):

        self.client = Client()


    def test_page_access(self):

        response = self.client.get("/test")

        self.assertEqual(response.status_code, 200)
