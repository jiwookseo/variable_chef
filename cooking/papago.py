import os
import urllib.request

client_id = os.getenv('NAVER_ID')
client_secret = os.getenv('NAVER_SECRET')


def translate(text):
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/language/translate"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    code = response.getcode()
    if code == 200:
        res = response.read().decode('utf-8')
        return True, res.split(',')[3].split(':')[2][1:-1].replace('.', '').lower()
    else:
        return False, None
