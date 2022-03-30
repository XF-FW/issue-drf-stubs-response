from rest_framework.test import APITestCase


class ExampleTest(APITestCase):
    def test_failure(self) -> None:
        response = self.client.get('/hello/', format="json")
        self.assertEqual(response.data["message"], "Hello, world!")
