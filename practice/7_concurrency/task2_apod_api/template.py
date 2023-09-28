import os
import requests
import concurrent.futures
from datetime import datetime, timedelta

API_KEY = "YOUR_KEY"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'

def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    metadata = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        url = f'{APOD_ENDPOINT}?api_key={api_key}&date={date_str}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('media_type') == 'image':
                metadata.append(data)
        current_date += timedelta(days=1)
    return metadata

def download_image(metadata):
    date = metadata['date']
    image_url = metadata['url']
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        filename = os.path.join(OUTPUT_IMAGES, f'{date}.jpg')
        with open(filename, 'wb') as image_file:
            image_file.write(image_response.content)
        print(f"Downloaded image for {date} and saved as {filename}")

def download_apod_images(metadata: list):
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_image, metadata)

def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)

if __name__ == '__main__':
    main()