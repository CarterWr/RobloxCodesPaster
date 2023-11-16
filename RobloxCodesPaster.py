"""
File: Roblox Codes Paster
Author: Carter Wright
Date:11/16/2023

Discription: This code file extracts roblox codes from a given text file already
containing roblox codes (add more on how to format the roblox code text files under)

Important Note: Before running this file make sure all dependencies are installed,
for information on how to install dependencies read the README file.

Potential improvements:
This method only currently works with roblox games where you just press enter after inputing
the code into the text box, so it can be improved by adding another function that makes it click
the enter box and then deletes. Once adding this there would need to be user input added to the
code to make it a option to select either pressing enter on the keyboard or clicking a enter box
in game.
"""



#Imports 
import pyautogui
from time import sleep as sleep

#file extraction function
def data_extractor():
    """
    Extracts roblox codes from the RobloxCodesList.txt File and removes white spaces
    and puts each code into a list and returns that list.
    
    Params: None

    Returns: codes_lst(list): List of extracted codes 
    """
    #Create empty list to store codes into
    codes_lst = []

    #Open up the RobloxCodesList.txt file
    with open('RobloxCodesList.txt', 'r') as file: #DO NOT CHANGE THE FILE NAME

        #Read all lines from file
        lines = file.readlines()
        
        #loops through each line in file
        for line in lines:
            #breaks loop if there is empty block spaces
            if (line.strip() == ""):
                break

            #cleans up the whitespaces 
            words = line.strip(' ')

            #sets code_lst to updated words
            codes_lst = words.split(" ")

            #filters out empty values
            codes_lst = list(filter(None, codes_lst))

            
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
            #instead of pyautogui hitting the enter key we wait for user input
            input(f"Press 'Enter' to continue, codes left: {index+1}/{len(lst)}")
            #give the user time again to click back into the text box after claiming
            sleep(3)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')


#Execution code
if __name__ == "__main__":
    #initalizing codes_lst to the list of codes returned by data_extractor()
    codes_lst = data_extractor()

    #display options to user 
    print("1 - auto paster (no clicking involved)")
    print("2 - manual paster (you must click the confirm button to contiue the clicks)")

    #gather user input after dispaly
    user_input = int(input())

    #run the code_paster function to automate pasting codes
    code_paster(codes_lst, user_input)
    

print("All of the codes have been used, Goodbye :)")