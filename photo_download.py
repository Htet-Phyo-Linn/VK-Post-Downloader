from header import *

def download_image_with_random_name(url, directory):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate a random filename
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.jpg'
    filepath = os.path.join(directory, filename)
    
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f'Image successfully downloaded : {filepath} \n')
    else:
        print(f'Failed to download image : {response.status_code} \n')


def photo_download(access_token, post_url, directory):

    # # Your VK access token
    # access_token = 'vk1.a.YG2OtRMlXFJhjw8NiaPG5YuksUBshM99-4BTzgr8r__bvbeZGPyE1t7arR8LqUef6BwB31MXR-8_1osSm9mAtnDfx1aBUzN_XZ3D1v1i4WGAQOB-04CStFsaxpgs0IU18PVuJdIuaftIYYahb44mJjtyu9yUq2bQp6FP7zXUgaLVxxfBCtCqfVpeUKSmrD5e'

    # Read post URL from file
    # with open('links.txt', 'r') as file:
    #     post_url = file.readline().strip()

    # Extract post owner_id and post_id from URL
    match = re.match(r'https://vk.com/wall(-?\d+)_(\d+)', post_url)
    if not match:
        raise ValueError("Invalid post URL")

    owner_id, post_id = match.groups()

    # API endpoint to get post details
    api_url = f'https://api.vk.com/method/wall.getById?posts={owner_id}_{post_id}&access_token={access_token}&v=5.131'

    # Make the request to the VK API
    response = requests.get(api_url)
    post_data = response.json()

    # Print API response for debugging
    # print(json.dumps(post_data, indent=4))

    # Function to extract orig_photo URLs from a post
    def extract_orig_photo_urls(post):
        return [
            attachment['photo']['orig_photo']['url']
            for attachment in post.get('attachments', [])
            if attachment['type'] == 'photo' and 'orig_photo' in attachment['photo']
        ]

    # Extract the orig_photo URLs from the main post and copy_history
    orig_photo_urls = []

    # Check the main response
    for post in post_data.get('response', []):
        # Extract from the main post
        orig_photo_urls.extend(extract_orig_photo_urls(post))
        
        # Extract from copy_history
        for history_post in post.get('copy_history', []):
            orig_photo_urls.extend(extract_orig_photo_urls(history_post))

    # Print the URLs
    for url in orig_photo_urls:
        download_image_with_random_name(url, directory)


    print("All photos downloaded successfully. \n")
