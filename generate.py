from header import *

def token_generate():
    # Replace these with your VK app credentials
    client_id = ''
    client_secret = ''
    redirect_uri = 'https://oauth.vk.com/blank.html'
    scope = 'video'

    # Step 1: Construct the VK OAuth URL
    auth_url = (
        f"https://oauth.vk.com/authorize?client_id={client_id}"
        f"&display=page&redirect_uri={redirect_uri}"
        f"&scope={scope}&response_type=code&v=5.131"
    )

    # Step 2: Open the URL in a web browser to authorize the app
    print(f"Opening the following URL in your browser to authorize the app: {auth_url}")
    webbrowser.open(auth_url)

    # Step 3: After authorization, you will be redirected to a URL with a code parameter
    authorization_code = input("Enter the authorization code from the URL: ")

    # Step 4: Exchange the authorization code for an access token
    token_url = (
        f"https://oauth.vk.com/access_token?client_id={client_id}"
        f"&client_secret={client_secret}&redirect_uri={redirect_uri}"
        f"&code={authorization_code}"
    )

    response = requests.get(token_url)
    data = response.json()

    return data

