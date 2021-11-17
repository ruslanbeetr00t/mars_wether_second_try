from pathlib import Path

try:
    file = Path('pythonProject6/mars_final/mars_photos.json').suffix == '.json'
except IOError:
    print('Error')

