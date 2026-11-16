import requests


def extract_data(base_url, token, action, function=None):
    
    url = f"{base_url}?action={action}"

    if function:
        url += f"&function={function}"

    url += f"&token={token}"

    print(f"Calling: {url}")

    response = requests.get(url)

    try:
        return response.json()
    except Exception:
        print(response.text)
        raise




