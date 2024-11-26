import requests

base_url = 'http://127.0.0.1:8080'

img_file = 'zoom.jpg'

def upload_image(file_path):

    url = f'{base_url}/upload'

    with open(file_path, 'rb') as image_file:

        files = {'image': image_file}
        response = requests.post(url, files=files)

    if response.status_code == 201:
        print('Upload Response:', response.json())
        return response.json()
    else:
        print('Upload Failed:', response.status_code, response.text)
        return None


def get_image(filename, content_type='text'):

    url = f'{base_url}/image/{filename}'
    headers = {'Content-Type': content_type}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        if content_type == 'text':
            print('Get Image URL Response:', response.json())

        elif content_type == 'image':
            with open(f'downloaded_{filename}', 'wb') as img_file:
                img_file.write(response.content)
            print(f'For content_type "image": downloaded_{filename}')
        return response

    else:
        print(f'Get Image Failed, expected code: {response.status_code}')
        return None


def delete_image(filename):
    url = f'{base_url}/delete/{filename}'
    response = requests.delete(url)

    if response.status_code == 200:
        print('Delete Successful:', response.json())
        return response.json()
    else:
        print(f'Delete Failed, expected code: {response.status_code}')
        return None


if __name__ == '__main__':

    upload_response = upload_image(img_file)
    uploaded_filename = upload_response.get('image_url', '').split('/')[-1]

    get_image(uploaded_filename, content_type='text')

    get_image(uploaded_filename, content_type='image')

    delete_image(uploaded_filename)
