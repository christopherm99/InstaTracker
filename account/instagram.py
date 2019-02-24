import json
import datetime
import subprocess
import os
from pathlib import Path
from geopy.geocoders import MapBox

def get_address_and_coordinates(query_str):
    geolocator = MapBox("pk.eyJ1IjoiY2FkMzE0IiwiYSI6ImNqc2ozaGQwYTF2bGk0OXM3Y3ltczI2aTYifQ.Txtofo3qGGSnep5GRu-vQw")
    location = geolocator.geocode(query_str)
    
    if hasattr(location, "longitude"):
        return str(location), location.latitude, location.longitude
    else:
        return str(location), 181, 181

def load_acc():
    data = json.load(open(os.path.join(os.path.dirname(__file__), Path("user_info.json"))))
    return data["username"], data["password"], data["token"]

login, pw, token = load_acc()

def get_config(user, directory):
    return ['instagram-scraper', user, '-u', login, '-p', pw, '-d', 'data', '--media-metadata', '--include-location', '--media-type', 'none', '--maximum', '100', '--quiet']

def scrape(user, directory):
    output = subprocess.check_output(get_config(user, directory)) # block until done
    return process_data(Path(directory))

def process_data(p):
    if not p.exists():
        return "Account not found", False
    location_url_str = "https://www.instagram.com/explore/locations/{}/{}" # id, slug
    post_url_str = "https://www.instagram.com/p/{}"
    location_query_str = "{}, {} {}. {}"
    location_str = "{}, {}. {}"

    data = json.load(open(p))
    ret_data = []
    for post in data:
        post_data = {}

        if post['location'] is None: 
            continue
        post_data["location_url"] = location_url_str.format(post['location']['id'], post['location']['slug']) if post['location']['has_public_page'] else None
        if post['location']['address_json']:
            addr_json = json.loads(post['location']['address_json'])
            post_data["location_name"] = location_str.format(post['location']['name'], addr_json['city_name'], addr_json['zip_code'])
            post_data["location_query"] = location_query_str.format(addr_json['street_address'], addr_json['city_name'], post["location"]["name"], addr_json['zip_code']) 
        else: 
            post_data["location_name"] = post['location']['name']
            post_data["location_query"] = post['location']['name']
        post_data["location_name"], post_data["latitude"], post_data["longitude"] = get_address_and_coordinates(post_data["location_query"])
        post_data["img_url"] = post['display_url']
        post_data["url"] = post_url_str.format(post['shortcode'])
        edges = post['edge_media_to_caption']['edges']
        post_data["text"] = edges[0]['node']['text'] if len(edges) > 0 else ""
        post_data["like_count"] = int(post['edge_media_preview_like']['count'])
        post_data["timestamp"] = int(post['taken_at_timestamp'])
        post_data["date"] = datetime.datetime.fromtimestamp(post_data["timestamp"]).strftime("%B %d, %Y")
        post_data["id"] = post['shortcode']
        ret_data.append(post_data)
    
    return ret_data, True
