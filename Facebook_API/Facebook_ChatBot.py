#!pip install facebook-sdk
from email.mime import message
#import facebook as fb
# Get Access token - Follow the video on how to get access token for your fb account
access_token = "EAASx6...YD3GiigZDZD"
# The Graph API allows you to read and write data to and from the Facebook social graph
#asafb = fb.GraphAPI(access_token)
#asafb.put_comment(object_id="me", message="Hell0o")
# Post a message in the facebook page
#a=asafb.put_object("me","feed",message = "This is automated post12345!")
#a=asafb.put_object(connection_name="me",parent_object="feed",data= "This is automated post1234y5!")
#a=asafb.put_object("me", "feed", message= "This is automated post1234y5!" )
#print(a['id'])

#asafb.put_comment("me", "comment", message= "This is automated post1234y5!")

'''
# Get the contents of a post
asafb.get_object("a['id']")
# Post a photo with captions
asafb.put_photo(open("meme.jpg","rb"), message = "Automated meme post")
# Comment on a post
asafb.put_object("a['id']","comments",message = "This is an automated comment!")

# Print the response
import requests
#api-end
url = ""
output = requests.get(url).json()
print(output)
'''