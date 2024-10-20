import requests

class YouTubeCRUD:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def create_video(self, title, description):
        # This is a placeholder function for creating a video
        return f"Video '{title}' created with description: {description}"

    def get_video(self, video_id):
        url = f"{self.base_url}/videos?part=snippet&id={video_id}&key={self.api_key}"
        response = requests.get(url)
        return response.json()

    def update_video(self, video_id, title, description):
        # This is a placeholder function for updating a video
        return f"Video '{video_id}' updated with title: {title} and description: {description}"

    def delete_video(self, video_id):
        # This is a placeholder function for deleting a video
        return f"Video '{video_id}' deleted"
