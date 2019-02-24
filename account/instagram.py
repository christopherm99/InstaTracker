import json
import datetime
import subprocess
import os
from pathlib import Path

def get_coordinates(query_str):
    return 0.0, 0.0

def load_acc():
    data = json.load(open(os.path.join(os.path.dirname(__file__), Path("user_info.json"))))
    return data["username"], data["password"]

login, pw = load_acc()

def get_config(user, directory):
    return ['instagram-scraper', user, '-u', login, '-p', pw, '-d', 'data', '--media-metadata', '--include-location', '--media-type', 'none', '--quiet']

def scrape(user, directory):
    subprocess.check_output(get_config(user, directory)) # block until done
    return process_data(Path(directory))

def process_data(p):
    location_url_str = "https://www.instagram.com/explore/locations/{}/{}" # id, slug
    post_url_str = "https://www.instagram.com/p/{}"
    location_str = "{}, {}. {}"

    data = json.load(open(p))

    ret_data = []
    for post in data:
        post_data = {}

        if post['location'] is None: 
            continue
        post_data["location_url"] = location_url_str.format(post['location']['id'], post['location']['slug']) if post['location']['has_public_page'] else None
        addr_json = json.loads(post['location']['address_json'])
        post_data["location_name"] = location_str.format(post['location']['name'], addr_json['city_name'], addr_json['zip_code'])
        post_data["location_query"] = location_str.format(addr_json['street_address'], addr_json['city_name'], addr_json['zip_code'])
        post_data["latitude"], post_data["longitude"] = get_coordinates(post_data["location_query"])

        post_data["img_url"] = post['display_url']
        post_data["url"] = post_url_str.format(post['shortcode'])
        edges = post['edge_media_to_caption']['edges']
        post_data["text"] = edges[0]['node']['text'] if len(edges) > 0 else ""
        post_data["like_count"] = int(post['edge_media_preview_like']['count'])
        post_data["timestamp"] = int(post['taken_at_timestamp'])
        post_data["date"] = datetime.datetime.fromtimestamp(post_data["timestamp"]).strftime("%B %d, %Y")
        post_data["id"] = post['shortcode']
        ret_data.append(post_data)
    
    return ret_data
