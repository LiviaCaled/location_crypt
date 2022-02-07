import time
import gps

key = 43

def encrypt(tstamp, location):
    now_low_res = int(tstamp / 300)
    now_bytes = now_low_res.to_bytes(5,"little")
    lat_bytes = int(location[0]).to_bytes(1, "little", signed=True)
    long_bytes = int(location[1]).to_bytes(2, "little", signed=True)
    text = now_bytes + lat_bytes + long_bytes
    _hash = []
    for l in text:
        _hash.append(l ^ key)
    return _hash


def decrypt(_hash):
    text = []
    for l in _hash:
        text.append(l ^ key)
    tstamp = int.from_bytes(text[0:4], "little")
    print("Decoded timestamp: %s" % (time.gmtime(tstamp),))
    lat = int.from_bytes(text[5], "little", signed=True)
    lng = int.from_bytes(text[6:7], "little", signed=True)

    return (time.gmtime(tstamp), lat, lng)

