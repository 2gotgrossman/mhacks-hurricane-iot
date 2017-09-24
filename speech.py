from IPython.display import Audio, display

# load speech file to process
blob_name = 'speech3.wav'
blob = blob_service.get_blob_to_bytes(container_name, blob_name)

wav_bytes = Audio(data=blob)
display(wav_bytes)

import requests
import urllib
import uuid

# Get access token to use the speech services
url_token_api = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken' # service address
api_key = '39f61de6d28e4667bbfda88dd37b12ce'          # Azure Cognitive API Key, replace with your own key

headers = {'Content-Length': '0', 'Ocp-Apim-Subscription-Key':api_key}

api_response = requests.post(url_token_api, headers=headers)

access_token = str(api_response.content.decode('utf-8'))


# Call Speech to text service
url_stt_api = 'https://speech.platform.bing.com/recognize' # service address

headers = {'Authorization': 'Bearer {0}'.format(access_token), \
           'Content-Length': len(blob), \
           'Content-type': 'audio/wav', \
           'codec': 'audio/pcm', \
           'samplerate': '16000'}

params = urllib.parse.urlencode({
    'scenarios': 'ulm',
    'appid': 'D4D52672-91D7-4C74-8AD8-42B1D98141A5', # dont change, it is fixed by design
    'locale': 'en-US', # speech in english
    'device.os': 'PC',
    'version': '3.0',
    'format': 'json', # return value in json
    'instanceid': str(uuid.uuid1()), # any guid
    'requestid': str(uuid.uuid1()),
})

api_response = requests.post(url_stt_api, headers=headers, params=params, data=blob)

import json
res_json = json.loads(api_response.content.decode('utf-8'))

print(json.dumps(res_json, indent=2, sort_keys=True))