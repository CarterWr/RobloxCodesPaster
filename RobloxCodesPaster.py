"""
File: Roblox Codes Paster
Author: Carter Wright
Date:11/16/2023

Discription: This code file extracts roblox codes from a given text file already
containing roblox codes (add more on how to format the roblox code text files under)

Important Note: Before running this file make sure all dependencies are installed,
for information on how to install dependencies read the README file.

Potential improvements:
Add it where the script grabs website data and looks for codes and pastes those codes to the 
RobloxCodesList.txt file.
"""



#Imports 
import pyautogui
from time import sleep as sleep
import requests
from bs4 import BeautifulSoup


#Website data getter funciton
def web_data_puller(url):
    """
    Finds and pulls codes from the link given

    Params: url(str): The url input given by the user

    Returns: Codes_lst(lst): A list of roblox codes provided by the given url
    """
    try:
        #Send a get request to url
        response = requests.get(url)

        #Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        #Finds the list items in the urls html code
        list_items = soup.find('body').find('ul')

        #creating a empty codes list to later store codes into
        codes_lst = []

        #Loop through list_items and find the codes and appending codes to codes_lst
        for item in list_items:
            strong_tags = item.find_all('strong')
            if len(strong_tags) > 0:
                code = strong_tags[0].get_text(strip=True)
                # Exclude phrases like "(New)"
                if "(New)" not in item.get_text(strip=True):  
                    codes_lst.append(code)

        print(codes_lst)
    
    except AttributeError as e:
        #Handles Attribute error
        print(f"Attribute error occured: {e}")
        print("Setting codes value to empty")

        codes_lst = []
    
    #return codes list
    return codes_lst




#auto code pasting function
def code_paster(lst, user_input):
    """
    Takes in the extracted codes and pastes each code

    Params: lst(list): The codes_lst that we got from extracting codes from file
            user_inpu(int): this will decide what paster the user will be using

    Returns: None
    """
    #Give user time to put cursor in the right spot 
    sleep(5)

    #if user_input does not equal either option, option 1 is default
    if user_input != 1 and user_input != 2:
        user_input = 1

    #checking for first iteration to display a print message once
    first_iteration = True

    #Loop through each code in the list
    for index, code in enumerate(lst):
        #if user picks option 1 the auto paste and enter runs
        pyautogui.write(code) 

        #This is for the games with no confirm box
        if user_input == 1:
            #presses enter automatically on the keyboard
            pyautogui.press('enter')
        #This is for the games with a confirm box
        elif user_input == 2:
            if first_iteration:
                input("Press 'ENTER' to continue")

            #give the user time again to click back into the text box after claiming
            sleep(3)
        
        #keeps track of how many codes are left
        print(f"codes left: {index+1}/{len(lst)}")
        
        #selects code and deletes it
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')


#Execution code
if __name__ == "__main__":
    #gets url user wants to get codes from
    codes_url = str(input("Enter codes website url: ")).strip()

    #Extracts codes from website and writes data onto RobloxCodesList.txt
    codes_lst = web_data_puller(codes_url)

    #chceks if the codes_lst is empty if it is ends script
    if len(codes_lst) == 0:
        print("There are no working codes!")
    #if there is codes in the codes list runs like normal
    else:
        #display options to user 
        print("1 - auto paster (no clicking involved)")
        print("2 - manual paster (you must click the confirm button to contiue the clicks)")

        #gather user input after dispaly
        user_input = int(input())

        #run the code_paster function to automate pasting codes
        code_paster(codes_lst, user_input)
        
        #ending statement
        print("All of the codes have been used, Goodbye :)")