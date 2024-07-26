from generate import *
from photoDownloadFile import *
from posttoLinks import *
from videoDownloadFile import *

def create_random_folder(base_path):
    """Create a random folder with a timestamp in the specified base path."""
    # Generate a random string
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Create the folder name
    folder_name = f"{random_str}_{current_time}"
    # Full path to the new folder
    folder_path = os.path.join(base_path, folder_name)
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def main(access_token):
        # Read URLs from links.txt
    if not os.path.exists('links.txt'):
        print("The file 'links.txt' does not exist.")
        return

    with open('links.txt', 'r') as file:
        urls = file.readlines()

    if not urls:
        print("No URLs found in 'links.txt'.")
        return


    for url in urls:
        url = url.strip()
        if url:
            extracted_urls = []
            base_path = "Downloads"

            random_folder = create_random_folder(base_path)
            print(f"Random folder created: {random_folder} \n")

            photo_download(access_token, url, random_folder)

            print(f"Extracting videos from: {url} \n")
            extracted_urls.extend(extract_video_urls(url))

            # Write extracted URLs to extract_links.txt
            with open('extract_links.txt', 'w') as file:
                for extracted_url in extracted_urls:
                    file.write(extracted_url + '\n')
                    print(f"Saved extracted URL to file: {extracted_url}\n")
            extract_file('extract_links.txt', random_folder)            

            extracted_urls.clear()



if __name__ == "__main__":
    
    data = token_generate()

    if 'access_token' in data:
        access_token = data['access_token']
        print(f"Access token obtained: {access_token}")

        main(access_token)
    

    else:
        print("Failed to obtain access token:", data)