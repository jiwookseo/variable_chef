import os
import urllib.request
import string

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
        word_list = res.split(',')[3].split(':')[2][1:-1].replace('.', '')
        res = ""
        for i in word_list:
            if i not in string.punctuation:
                res += i
        return True, " ".join(res.lower().split())
    else:
        return False, None


if __name__ == "__main__":
    print(translate(input()))
