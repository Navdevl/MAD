#!/usr/bin/python

# Author: Naveen
# Github: @navdevl

import requests
import json
import urllib2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("link", help="provide the link of the article you wanted to grab", type=str)
parser.add_argument("download_location", help="provide the destination to download the file", nargs='?', default=os.getcwd())
args = parser.parse_args()

medium_url = args.link
medium_id = medium_url.split('-')[-1]

medium_notes_url = "https://medium.com/p/{0}/notes".format(medium_id)

response = requests.get(medium_notes_url)
response_string = response.content.split('</x>')[-1]

response_object = json.loads(response_string)

duration = response_object['payload']['post']['audioVersionDurationSec']

if duration > 0:
  medium_audio_url = response_object['payload']['post']['audioVersionUrl']
else:
  print("Sorry. I can't find any audio for this article. Just go read.")
  exit()

response = urllib2.urlopen(medium_audio_url)
medium_audio = response.read()
save_file_extension = medium_audio_url.split('.')[-1]
save_file_name = "{0}.{1}".format(medium_id, save_file_extension)
save_file_location = os.path.join(args.download_location, save_file_name)


with open(save_file_location,'w') as output:
  output.write(medium_audio)
