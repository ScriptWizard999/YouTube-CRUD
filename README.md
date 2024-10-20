# YouTube-CRUD

A simple Python package to perform basic CRUD operations on YouTube using the YouTube Data API.

## Installation

```bash
pip install youtube-crud
```
## Usage

``` python
from youtube_crud.youtube import YouTubeCRUD

youtube = YouTubeCRUD(api_key="your_api_key")

# Create a video
youtube.create_video("Title", "Description")

# Get video details
youtube.get_video("video_id")

# Update a video
youtube.update_video("video_id", "New Title", "New Description")

# Delete a video
youtube.delete_video("video_id")
```
