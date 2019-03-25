#/usr/etc/env python
"""
2019.03 Dang Doan


Code speech to text with Google cloud:

Convert WAV to FLAC, by running sox in terminal:

sox input.wav output.flac

or use FFMPEG to convert MP3 to FLAC in terminal:

ffmpeg -i input.mp3 output.flac

Upload file to Google Cloud Storage folder (if running gcloud with a file from computer, the file must be less than 10MB) via web browser: https://console.cloud.google.com/storage/browser/

or use the gsutil in terminal, e.g.:

gsutil cp output.flac gs://dang_gstorage/speech/

Run gcloud in terminal:

dang@KubuntuElite:~/google_cloud/google-cloud-sdk/bin$ ./gcloud ml speech recognize-long-running ‘gs://dang_gstorage/ZOOM0005_Tr1.flac‘ --language code=’vi-VN’ --async
-> output:
Check operation [607280323405008030] for status.
{
“name”: “607280323405008030”
}

Test command:
dang@KubuntuElite:~/google_cloud/google-cloud-sdk/bin$ ./gcloud ml speech operations wait 607280323405008030

Collect data when done:

dang@KubuntuElite:~/google_cloud$ gcloud ml speech operations describe 607280323405008030 > test_transcribe_vn.json

Then use this function:

postprocess_json(‘test_transcribe_vn.json’)

"""

import json

def postprocess_json(google_json_file):
    with open(google_json_file, 'rt') as json_file:
        data = json.load(json_file)
    for result in data['response']['results']:
        print(result['alternatives'][0]['transcript'])
        print('Confidence: '+str(result['alternatives'][0]['confidence']))
