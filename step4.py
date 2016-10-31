import urllib2,json, ast

url = 'http://challenge.code2040.org/api/prefix'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961'}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
dictionary = ast.literal_eval(response.read())

prefix = dictionary["prefix"]
array = dictionary["array"]

def find_strings(prefix, array):
	no_prefix_array = []
	for s in array:
		if s.startswith(prefix) == False: 
			no_prefix_array.append(s)
	return no_prefix_array
	
final_array = find_strings(prefix,array)		
url = 'http://challenge.code2040.org/api/prefix/validate'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961', 'array': final_array}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)
response = urllib2.urlopen(req,data)