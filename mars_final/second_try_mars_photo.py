import json
import requests
from nasa_api import API
from commands_nasa import *
from path_except import *


def user_input_data():
    try:
        year = int(input(year_messages))
        month = int(input(month_messages))
        day = int(input(day_messages))
        if len(str(year)) == 4 and len(str(month)) == 2 and len(str(day)) == 2:
            data_photo_mars_photo = f'{year}-{month}-{day}'
            print(data_photo_mars_photo)
            return str(data_photo_mars_photo)
        else:
            print(validator_data)
    except ValueError:
        print(user_input_except)
        return user_input_data()


def user_parameters():
    data_photo = user_input_data()
    my_parameter = {'api_key': API,
                    'earth_date': data_photo}
    return my_parameter


def response_user_url():
    try:
        parameter = user_parameters()
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        response = requests.get(url, params=parameter)
        if response.status_code == 200:
            return response.json()
    except ConnectionError:
        print(connection_error_messages)


def write_json_file():
    with open('mars_photos.json', 'w', encoding='utf-8') as file_json:
        json.dump(response_user_url(), file_json, ensure_ascii=False, indent=4)
    return 'mars_photos.json'



def read_json():
    with open(write_json_file(), 'r', encoding='utf-8') as file_json:
        read_info = json.load(file_json)
        for photos in read_info['photos']:
            all_photos = photos['img_src']
            print(all_photos)


read_json()

