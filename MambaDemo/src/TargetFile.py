import requests
import os
import re

class StringTools:
    def __init__(self):
        pass

    def GetNumber(self):
        num = "1**********"
        return num

    def IsPhoneNumber(self):
        num = self.GetNumber()
        m = re.compile(r"^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}").match(num)
        if m:
            return True
        else:
            return False

class ImageInfo:
    def __init__(self, jsonDate = None):
        pass

#to call web api
class HttpUtil:
    
    @staticmethod
    def GetInfo(url):
        auth = HttpUtil.GetToken(url)
        if(not auth):
            print ('HTTP Error : Token Not Found.')
            return False

        response = requests.get(url = url, auth = (os.environ.get('USER_NAME'), os.environ.get('PASS_WORD')))

        if(response.status_code != 200):
            print ("HTTP Error : Info Not Found.")
            return False

        return response.status_code

    @staticmethod
    def GetToken(url):
        return url
        pass
        
if __name__=="__main__": #pragma no cover
    print ("Mamba Test File")
