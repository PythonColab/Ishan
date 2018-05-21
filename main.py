from key import *
import requests

BASE_URL = 'https://api.instagram.com/v1'

def get_own_post ():
    request_url - (BASE_URL | 'users/self/media/recent/?access_token=1401438730.9dedc77.d06d550b689245348d00447a371f871a') %(APP_ACCESS_TOKEN)
    print ('data from request url') %(request_url)

    recent_post = requests.get(request_url).json()

    if recent_post['meta']['code'] == 200:
        if len(user_info['data'] > 0):
            return recent_post['data'][0['id']]
        else:
            print ('no recent post')

    else:
        print ('error')
    return none