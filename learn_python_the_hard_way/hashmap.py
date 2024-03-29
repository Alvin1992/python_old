def new(num_buckets = 256):
	"""Initilize a Map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	"""Given a key this will creat a number and then convert it to an index for the aMap's buckets."""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default = None):
	"""
	Return the index, key, and value of a slot found in a bucket.
	Return -1, key, default(None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k , v
	return -1, key, default

def get(aMap, key, default = None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default = default)
	return v

def set(aMap, key, value):
	"""Sets the key to the value, replacing any exiting value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >= 0:
		#the key exits, replace it
		bucket[i] = (key, value)
	else:
		#the key does not, append to creat it
		bucket.append((key, value))

def delete(aMap, key):
	"""Delete the given key from the Map."""
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""Print out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v