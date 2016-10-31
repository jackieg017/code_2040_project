import urllib2,json, ast, datetime

url = 'http://challenge.code2040.org/api/dating'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961'}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
dictionary = ast.literal_eval(response.read())

date_stamp = dictionary["datestamp"]
print(date_stamp)
interval = dictionary["interval"]


def add_seconds(date_stamp, interval):
	ISO_8601_FORMAT = '%Y-%m-%dT%H:%M:%SZ' 
	stamp = datetime.datetime.strptime(date_stamp, ISO_8601_FORMAT)
	increment = datetime.timedelta(seconds=interval)
	stamp = stamp + increment
	stamp = stamp.strftime('%Y-%m-%dT%H:%M:%SZ')
	print(stamp)
	return stamp

updated_stamp = add_seconds(date_stamp, interval)
		
url = 'http://challenge.code2040.org/api/dating/validate'
postdata = {'token':'3bcc66432859f116f85e48a7bce43961', 'datestamp': updated_stamp}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)
response = urllib2.urlopen(req,data)