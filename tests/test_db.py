import unittest

from app.database.lib import Database
from app.database.models.post import Post


MODELS = [Post]
TEST_DB = Database.get_instance()


class TestPost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        # TEST_DB.bind(MODELS, bind_refs=False, bind_backrefs=False)
        # TEST_DB.connect()
        TEST_DB.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        TEST_DB.drop_tables(MODELS)
        # TEST_DB.close()

    def test_post(self):
        # Create 2 posts
        first_post = Post.create(
            name='Joe Doe', email='joe@example.com', content='Hello word, I\'m John!')
        second_post = Post.create(
            name='Jane Doe', email='jane@example.com', content='Hello word, I\'m Jane!')

        assert first_post.id == 1
        assert second_post.id == 2

        # Get posts and assert that they are correct
        posts = Post.select().execute()

        assert len(posts) == 2
