from fastapi.testclient import TestClient  # type: ignore
from fastapi import Response  # type: ignore
from run_app import app
from unittest import TestCase


class TestArticlesViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_hellow_world_success(self) -> None:
        response: Response = self.client.get("/v1/articles/hello")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})
