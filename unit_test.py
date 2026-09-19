import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(
            data["message"],
            "Welcome to My Page, Greetings by Hamza",
        )
        self.assertEqual(data["platform"], "GitHub Actions")
        self.assertEqual(data["runtime"], "Docker + Flask")

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()

        self.assertEqual(data["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
