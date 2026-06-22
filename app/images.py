from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

# IMAGEKIT_URL is the public CDN URL for delivered assets.
# Use the default ImageKit API URL for uploads instead of overriding base_url.
imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
)