import requests 
class MyAuth(requests.auth.AuthBase):
      def __call__(self,r):
          return r 	


if __name__ == "__main__" :
    url = 'http://httpbin.org/get'
    resp=requests.get(url, auth=MyAuth())
    print resp
