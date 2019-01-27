# vault_analyzer
A Python program to analyze Fallout Shelter vaults. Inspired by https://github.com/rakion99/shelter-editor.

## What is vault_analyzer?
*vault_analyzer* is a tool written in Python 3.7 that reads decrypted Fallout Shelter vault save files and presents data about the vault. It shows the average health, level, SPECIAL attributes, and weapon of vault dwellers.

*vault_analyzer* should prove useful to those who wish to gain an upper hand in their game of Fallout Shelter without actually editing the save file. Think of it as a census for your vault.

## How do I use vault_analyzer?
*vault_analyzer* is a simple Python 3.7 script. Clone this repository to your local machine. The real trick is getting the save file from your game. Retrieve it from your device's storage, and go to [this website](https://fossd.netlify.com/) to convert it into JSON. Place the JSON file into the directory of the cloned project. Run `python vault_analyzer.py <file_name>.json` at a command prompt to get your results. 
