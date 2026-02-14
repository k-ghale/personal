

cache = {}

def is_cache_there(url):
    if cache.get(url):
        print("cache already there")
        return cache[url]
    else:
        cache[url] = True # get_data_from_url(url)
        data = cache[url]  
        print("cache accepted")



is_cache_there("google.com")
is_cache_there("yahoo.com")
is_cache_there("google.com")
