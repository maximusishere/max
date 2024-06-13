import hashlib

class MarsURLEncoder:

    def __init__(self):
        self.url_join = {}

    def encode(self, long_url):
        self.long_url = long_url
        url1 = 'https://ma.rs/' # ('/'.join(long_url.split('/')[:3])) + '/'
        long_url2 = long_url
        long_url = ('/'.join(long_url.split('/')[3:]))
        hash_object = hashlib.sha256(long_url.encode())
        hash_digest = hash_object.hexdigest()
        hash_short = hash_digest[:10]
        self.hash_mash = url1 + hash_short
        self.url_join[self.hash_mash] = long_url2
        return str(self.hash_mash)

        # part_for_hash = ('/'.join(long_url.split('/')[3:]))

    def decode(self, short_url):
        self.short_url = short_url
        short_url = self.url_join[self.hash_mash]
        return short_url


mars_url = MarsURLEncoder()
url = 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
er =  'werewfewfdfewf'
print(mars_url.encode(url))
print(mars_url.encode(er))
print(mars_url.encode(url))
