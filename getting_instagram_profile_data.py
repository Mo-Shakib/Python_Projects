# this code can give instagram user information
from bs4 import BeautifulSoup 
import requests 
URL = "https://www.instagram.com/{}/" # instagram URL 

def acc_data(s): #account function 
    data = {} 
    s = s.split("-")[0] # splittting the content and taking forst part
    s = s.split(" ")  # again splitting the content  
    data['Followers'] = s[0] # assigning the values 
    data['Following'] = s[2] 
    data['Posts'] = s[4] 
    return data 

def url_data(username): # url function
    r = requests.get(URL.format(username))  # getting the request from url 
    s = BeautifulSoup(r.text, "html.parser")  # converting the text 
    meta = s.find("meta", property ="og:description") # finding meta info 
    return acc_data(meta.attrs['content']) 
  
if __name__=="__main__": # main function 
    username = input('Enter the username: ') # user name 
    data = url_data(username) 
    print(data) # printing the info 