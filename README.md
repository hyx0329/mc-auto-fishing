# Minecraft Auto Fishing
*inspired by: [Rob Dundas](https://medium.com/geekculture/lets-go-fishing-writing-a-minecraft-1-17-auto-fishing-bot-in-python-opencv-and-pyautogui-6bfb5d539fcf)*

*about how to figure out a window's position and dimentions on linux: [check here](https://unix.stackexchange.com/questions/14159/how-do-i-find-the-window-dimensions-and-position-accurately-including-decoration)*

## Intro

+ Minecraft auto fishing script
+ NO OpenCV requirement
+ **this project "just work" and will not be further developed**
+ use `pipenv` to manage python packages
+ Windows is not supported(but you can)

## Usage

prepare the environment:

+ `pipenv install` or `pip install -r requirements.txt`

to start auto fishing:

+ launch the game(in windowed mode)
+ go to your fishing spot
+ press esc(to open the game menu)
+ run the script `mc_auto_fishing.py`, and just wait(remember to activate pipenv's shell if using it)
+ tweak Steve's/Alex's position if necessary

to stop auto fishing:

+ change focus to another window
