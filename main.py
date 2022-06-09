import pandas as pd

import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('qtbltFawvaNkZWX8B2-j4A', 'R9ZlzLpu3F8GUIRbEDk7WJ9vkomvuw')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'Freduccini',
        'password': 'hfyvadqx1'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'TikTokGenerator/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

# def main():
res = requests.get("https://oauth.reddit.com/r/python/hot", headers=headers, params={'limit': '100'})

df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
# TODO port to pd.concat
for post in res.json()['data']['children']:
    # append relevant data to dataframe
    df = pd.concat([df, pd.DataFrame({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, index=[0])], ignore_index=True)

df.head()

#
# if __name__=='__main__'
#     main()
