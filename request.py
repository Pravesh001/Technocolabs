import requests

url = 'https://pravesh-spotify-skip-pred.herokuapp.com/predict'
r = requests.post(url,json={'session_p':1, 'session_l':20, 'no_pause':0,
                            'long_pause':0,'acoustic':1,'live':0,'acousticv6':1})

print(r.json())
