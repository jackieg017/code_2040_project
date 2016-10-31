import urllib2,json, ast

url = 'http://challenge.code2040.org/api/haystack'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961'}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
haystack_dictionary = ast.literal_eval(response.read())

needle = haystack_dictionary["needle"]
haystack = haystack_dictionary["haystack"]

def find_needle(needle, haystack):
	index = 0
	for i in range(len(haystack)):
		if haystack[i] == needle:
			index = i
			break 
	return index
	
index = find_needle(needle,haystack)		
url = 'http://challenge.code2040.org/api/haystack/validate'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961', 'haystack': index}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)
response = urllib2.urlopen(req,data)