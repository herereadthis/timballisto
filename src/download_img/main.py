import os
import requests

# URL pattern and directory for images
base_url = "https://online.anyflip.com/sqtpd/mcdg/files/mobile/"
output_folder = "./img/"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Total number of images
total_images = 448

# Download images
for i in range(1, total_images + 1):
    # Construct the image filename without zero-padding for URL
    original_filename = f"{i}.jpg"
    url = f"{base_url}{original_filename}"

    # Construct the image filename with zero-padding for local storage
    padded_filename = f"{i:03}.jpg"
    filepath = os.path.join(output_folder, padded_filename)

    # Check if the file already exists
    if os.path.exists(filepath):
        print(f"{padded_filename} already exists, skipping...")
    else:
        # Download the image
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {original_filename} as {padded_filename}")
        else:
            print(f"Failed to download {original_filename}")
