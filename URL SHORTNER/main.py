import pyshorteners

# Function to shorten URL
def shorten_url(url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url

# Main code
url_to_shorten = "https://www.example.com"

shortened_url = shorten_url(url_to_shorten)
print("Shortened URL:", shortened_url)
