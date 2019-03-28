# WogglAI-FuctionalScript
Jez Whitworth Create an AI chatbot called "Woggle" but as the years have gone by the scripts have become out dated and don't function anymore, we have fixed that but unforunetly the question system that allows woggle to go to the internet and bring back information no longer works but you still get the AI.

# Step 0 - Preperation
Make sure you have a raspberry pi with an sd card in it running resbian (It's fine to be running resbian on noobs)
Then check to make sure your version of resbian, python 3, and wolfram are up to date or download python 3 for windows or mac

# Step 1
Download the program files from Github (These with replce the files Jez Whitworth have provided)

# Step 2
Watch this video https://www.youtube.com/watch?v=tW1TM8m429Q which will explain how to create a Wolframalpha account and how to get your appid and then on windows, open command prompt or search cmd on windows, then type: pip install wolframalpha api, then press enter. or on mac open command prompt ( i dont know the name on mac ) then do the exact same thing

# Step 3
Open the "Chat" script in a text editor by right clicking it and the go to "open with" (DO NOT OPEN IN PYTHON YET) on windows right click the chat.py, and then press edit with IDLE

# Step 4
In the chat script go to line 55 and where it says 'here' paste your code so it looks like this: 'Your appid here' to get the appid look at step 2, and go to line 60 and change it to where you keep you conversation.sqlite

# Step 5 
Put the Chat script along with any SQ files onto an external storage device that you can put into your rasberry pi, if on windows just do nothing

# Step 6
Once your raspberry pi is booted open the start menu and open python 3 (IDLE), In the top left press file, then open and find the directory of the Chat file. You will see another window woth the script open up, got to the top and press run, then Run Module.

# Step 7 - Enjoy
I hope this helps, if it dosen't please contact me here on github, Please note that these instructions are for people using windows and want Woggle running on there raspberry pi, if your using Mac, you can try to the best of your abilities but I'm sorry if it dosen't work the same.
