import urllib2,json

url = 'http://challenge.code2040.org/api/reverse'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961'}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
string_to_reverse = str(response.read())

def reverse_string(some_string):
	return some_string[::-1]

reversed_string = reverse_string(string_to_reverse)
url = 'http://challenge.code2040.org/api/reverse/validate'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961', 'string': reversed_string}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)
response = urllib2.urlopen(req,data)
