import grequests
import time

start_time = time.time()
# Create a 10000 requests
urls = [grequests.post("http://localhost:5000/api/auth/signin", json={
	"usernameOrEmail" : "minhlevan104@gmail.com",
	"password" : "minh123"
})] * 1000
# rs = (grequests.head(u) for u in urls)
print("xong tao url")
# Send them.
res = grequests.map(urls)

print( time.time() - start_time) # Result was: 9.66666889191