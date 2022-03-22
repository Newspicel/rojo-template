import requests
import os

switch = {
            409: "User is not authorized to access Asset.",
            404: "Asset not found."
        }

def downloadPlace(placeID, auth):

    headers = {
        'authority': 'assetdelivery.roblox.com',
        'sec-ch-ua': '"(Not(A:Brand";v="8", "Chromium";v="99", "Google Chrome";v="99"',
        'accept': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://assetdelivery.roblox.com/docs',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6',
        'cookie': ".ROBLOSECURITY=" + auth,
        'dnt': '1',
        'sec-gpc': '1',
    }

    result = requests.get("https://assetdelivery.roblox.com/v1/assetId/" + placeID, headers=headers)

    if result.status_code == 200:

        url = result.json()["location"]

        result = requests.get(url)

        if result.status_code == 200:
            print("Downloading place: " + placeID)
            return result.content
        else:
            if result.status_code in switch:
                print(str(result.status_code) + " : " + switch[result.status_code])
            else:
                print("Error: " + result.status_code)

#save to file
with open(os.getcwd() + '/.remodel/place.rbxl', 'wb') as file:
    file.write(downloadPlace(os.environ['ASSETID'], os.environ['ROBLOSECURITY']))
