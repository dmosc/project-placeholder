from app import app
from app.database.lib import Database
from app.database.models.post import Post
import unittest


MODELS = [Post]
TEST_DB = Database.get_instance()


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        TEST_DB.create_tables(MODELS)

    def tearDown(self):
        TEST_DB.drop_tables(MODELS)

    def test_home_page(self):
        response = self.client.get("/")
        html = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<title>Week 1 - Team Portfolio</title>" in html
        assert "text/html; charset=utf-8" == response.headers["Content-Type"]

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        html = response.get_data(as_text=True)

        assert response.status_code == 200
        assert "<title>MLH Timeline</title>" in html
        assert "text/html; charset=utf-8" == response.headers["Content-Type"]

    def test_get_posts(self):
        response = self.client.get("/api/get_posts")
        json = response.get_json()

        assert response.status_code == 200
        assert "posts" in json
        assert len(json["posts"]) == 0

    def test_create_post(self):
        response = self.client.post(
            "/api/create_post", data={"name": "Test", "email": "test@test.com", "content": "testhello"})
        saved_posts = Post.select().execute()

        assert len(saved_posts) == 1
        assert response.status_code == 302

    def test_malformed_timeline_post(self):
        # Handle missing name parameter
        response = self.client.post(
            "/api/create_post", data={"email": "test@test.com", "content": "testhello"})

        assert response.status_code == 400

        # Handle empty content
        response = self.client.post(
            "/api/create_post", data={"name": "test", "email": "test@test.com", "content": ""})

        assert response.status_code == 400

        # Handle malformed email
        response = self.client.post(
            "/api/create_post", data={"name": "test", "email": "not-email", "content": ""})

        assert response.status_code == 400
