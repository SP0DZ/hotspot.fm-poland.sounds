# import urllib library
from urllib.request import urlopen
import json
url = "http://reflector.fm-poland.pl/api/tgdb.json"
response = urlopen(url)
data_json = json.loads(response.read())
for key in data_json:
        value = data_json[key]
        print("[{}] => [{}]".format(key, value[2:]))
        f = open( "talk_group-" + str(key) + ".txt","w")
        f.write(value[2:])
        f.close()
pass
