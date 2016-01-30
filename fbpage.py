import urllib2
import json

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.5/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,description,likes,link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

page_id = "PAGE ID" # username or id
token = "ACCESS TOKEN"  # Access Token
page_data = get_page_data(page_id,token)

print json.dumps(page_data)
print "Likes:"+ str(page_data['likes'])
