
Create a short URL generator where it will work with input values that are either a standard URL or a comma -deliminated lists of URLs.
The expeted output is a corresponding shortend URL representation consisting of a short(and fixed) domain name followed by an 8-character URI. 
Implement this with code golf concept in mind,meaning with a tight algorithmic implementation snf low memory usage.

The resulting URL will be in the secire URL using the sf.ly doamin.
The URI will be the firdt 8 characters of a SHA-1 hash value using the origin (input) URL as the source. 
A SHA-1 hash value is typically rendered as a hexadecimal number, 40 characters long.
you do not need to implement SHA-1 cryptographic hash function, please use the existing math fucntionalities in the programming language of choice(PHP/Python)

----------------------------
import hashlib
def generateShortUrl(OriginUrl):
  count = 0 
  list= OriginUrl.split(,)
  for x in range(0,len(list)):
    abc = list[x]
    m = hashlib.sha1(abc.encode('utf-8'))
    m = m.hexdigest()
    m = m[count: count+7]
    count = count + 1
  return 'https://sf.ly/' + m
  
  ----------
  code working for case 1 only 
