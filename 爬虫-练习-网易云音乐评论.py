import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json

'''
function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
f = 00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
function d(d, e, f, g) {   d = data,  e=010001  f = f  g =  0CoJUm6Qyw8W8jud
    var h = {}
      , i = a(16);    i = 随机16个字符
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}
'''

url = "https://music.163.com/weapi/comment/resource/comments/get"
data = {
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "2000",
    "rid": "R_SO_4_33497051",
    "threadId": "R_SO_4_33497051"
}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "QE4Ur5calyLz1P9l"
encSecKey = "7ff2863a4511730760ee528a7dedb1b09a3cd429bd02158c9d6bb45c41d5ac33291c9f29716862b9ab4833f744d8326824ec0c74d4e543c8ef8bdb8bc465cf237bc7bdfa6f2aab37f86fe3dbfba10875cb5937bd66c30bd6b1022793342dc5cad17251767c8d16024155f1fe807cae7517d782d3c11d5a1d7fd4febce85a97a7"

def get_enc_param(data):
    return enc_param(enc_param(data, g), i)

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data
def enc_param(data, key):
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV="0102030405060708".encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8")); #加密
    return str(b64encode(bs), "utf-8")


resp = requests.post(url, data = {
    "params" : get_enc_param(json.dumps(data)),
    "encSecKey" : encSecKey
})
for user in resp.json()['data']['hotComments']:
    print(user['content'])