import requests


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("No photos found for the given parameters.")

    else:
        for index, photo in enumerate(photos[:2], start=1):
            img_url = photo.get('img_src')

            if img_url:
                print(f"Downloading photo {index} from {img_url}")

                img_response = requests.get(img_url)

                if img_response.status_code == 200:
                    filename = f"mars_photo{index}.jpg"

                    with open(filename, 'wb') as file:
                        file.write(img_response.content)
                        print(f"Saved {filename}")

                else:
                    print(f"Failed to download photo {index}.")
else:
    print(f"Failed to fetch data from API. Status code: {response.status_code}")
