import urllib.request,json
from models import News, Articles

# Getting api key
apiKey = None
# Getting the news base url
base_url = None
# Getting the articles base url
articles_url = None

def configure_request(app):
	global apiKey,base_url,articles_url
	apiKey = app.config["NEWS_API_KEY"]
	base_url = app.config["NEWS_API_BASE_URL"]
	articles_url = app.config["ARTICLES_BASE_URL"]