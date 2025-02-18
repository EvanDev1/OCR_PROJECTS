import requests

api_url = "https://api.vi-o.tech/v1/market/items"
api_key = "5d7d26a2-59ed-40ea-b45b-d46b9f3bfcd9"

headers = {
    "x-api-key": api_key,
}

def get_item_list():
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        item_list = response.json()
        # filtered_array = filter_items(item_list)
        return item_list
    else:
        print("Failed to fetch data:", response.text)
        return None

def filter_items(item_list):
    # words_to_filter = ['Ancient', 'Ethereal', 'Dread', 'Hybrid', 'Uniform', 'Pants', 'T-Shirt', 'Damaged', 'Axnit', 'Narcor', 
    #                    'Reknite', 'Korrelite', 'Vexnium', 'Water', 'Swap', 'Trade', 'Nebula', 'Neon', 'Firework', 
    #                    'Banner', 'Gellium', 'Chair', 'shelf', 'Couch', 'Counter', 'Bench', 'Projector', 'House', 'Stand', 'Wall', 
    #                    'Table', 'Blueprint', 'Mission', 'tag', 'bed', 'counter', 'display', 'table', 'plant', 'crate', 'snowball', 'starflee', 'flower', 'globe', 'green fade', 'hourglass', 'ice and fire', 'icy blue', 'imperial armada', 'integrated circuit', 'jolly roger', 'lucky seven', 'lunar', 'meteor', 'mining guild', 'nebula', 'neon', 'nuclear', 'orange', 'one alpha', 'pink fade', 'patriotic trail', 'fade', 'pure', 'rainbow', 'recycled', 'swap', 'trade union', 'syndicate', 'zero alpha']
    filtered_array = []

    # for item in item_list:
    #     should_add = True
    #     for word in words_to_filter:
    #         if word.lower() in item.lower():
    #             should_add = False
    #             break
    #     if should_add:
    #         filtered_array.append(item)

    for item in item_list:
        if 'shrapnel' in item.lower() and 'dread' in item.lower() :
            filtered_array.append(item)

    return filtered_array

for item in get_item_list():
    print('"' + item + '",')