import re
import urllib.request

url = input('Enter a url here: ')

if not url.startswith('http'):
    url = 'http://' + url
response = urllib.request.urlopen(url)
html = response.read().decode()

link_counter = len(re.findall(r'<a .*?href=".*?".*?>.*?<\/a>', html))

br_counter = len(re.findall(r'<br .*?/?>', html))
br_counter += len(re.findall(r'<p .*?>.*?<\/p>', html))

print('The page has %s links. ' % link_counter)
print('The page has %s newlines. ' % br_counter)
