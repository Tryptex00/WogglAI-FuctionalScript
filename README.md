# WogglAI-FuctionalScript
Jez Whitworth Create an AI chatbot called "Woggle" but as the years have gone by the scripts have become out dated and don't function anymore, we have fixed that but unforunetly the question system that allows woggle to go to the internet and bring back information no longer works but you still get the AI.

# NOTE - Before Starting
Since this modified version of woggle was created here on Github, Jez Whitworth has created an online version Here: https://repl.it/@rustyrocket/Chatterbox that can be run in a web browser without any of the steps below, however, Woggle won't remember your conversations with him or learn from what you teach him if you run it in the web browser. If you want Woggle to remember the conversations you had with him and learn from them then you will need to run it locally on your raspberry pi, which means you will still need this guide for that. So to summarize, if you don't need Woggle to learn or just want to try him out, you can go to the web link, but if you want to be able to run woggle without Wifi on a raspberry pi and be able to learn, you will need this guide.
# Step 0 - Preperation
Make sure you have a raspberry pi with an sd card in it running resbian (It's fine to be running resbian on noobs)
Then check to make sure your version of resbian, python 3, and wolfram are up to date

# Step 1
Download the program files from Github (These with replce the files Jez Whitworth have provided)

# Step 2
Watch this video https://www.youtube.com/watch?v=tW1TM8m429Q which will explain how to create a Wolframalpha account and how to get your appid

# Step 3
Open the "Chat" script in a text editor by right clicking it and the go to "open with" (DO NOT OPEN IN PYTHON YET)

# Step 4
In the chat script go to line 55 and where it says 'here' paste your code so it looks like this: 'Your appid here'

# Step 5 
Put the Chat script along with any SQ files onto an external storage device that you can put into your rasberry pi

# Step 6
Once your raspberry pi is booted open the start menu and open python 3 (IDLE), In the top left press file, then open and find the directory of the Chat file. You will see another window woth the script open up, got to the top and press run, then Run Module.

# Step 7 - Enjoy
I hope this helps, if it dosen't please contact me here on github, Please note that these instructions are for people using windows and want Woggle running on there raspberry pi, if your using Mac, you can try to the best of your abilities but I'm sorry if it dosen't work the same.
