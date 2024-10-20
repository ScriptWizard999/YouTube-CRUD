import unittest
from youtube_crud.youtube import YouTubeCRUD

class TestYouTubeCRUD(unittest.TestCase):
    def setUp(self):
        self.youtube = YouTubeCRUD(api_key="AIzaSyAsLeRZJmK2ZCsT5NjR5LXJA64KNYQp7h4")

    def test_create_video(self):
        result = self.youtube.create_video("Test Title", "Test Description")
        self.assertIn("Video 'Test Title' created", result)

    def test_update_video(self):
        result = self.youtube.update_video("12345", "Updated Title", "Updated Description")
        self.assertIn("Video '12345' updated", result)

    def test_delete_video(self):
        result = self.youtube.delete_video("12345")
        self.assertIn("Video '12345' deleted", result)

if __name__ == '__main__':
    unittest.main()
