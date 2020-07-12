# Welcome to RandKat
## Indecisive about what Kattis Question to do next?
### Then you came to the right place!!!


#### What are the features of this repo?
Generate a random kattis Question, Open a kattis Question based on its ID, Save a Question as .html file(__Coming Soon!__)

### Setup
First you will need to install three packages, copy and paste into the command Line to install

	- "pip3 install bs4"
	- "pip3 install fake-useragent"
	- "pip3 install requests"

Next you will need to update the data.txt file if it hasnt been updated in a while.
To do this just run the "dataWrite.py" file on your command line

	- python dataWrite.py

This will print out numbers, the pages of tables on the Open.Kattis.com website, scraping the problemId
with difficulty. It will print "Finished" when executed.

## Instructions:
### katRand
This program will open a random Kattis Question in a new Tab based on what difficulty parameters you want.
	eg.
	LowerBound = 1.3
	UpperBound = 4.6
	The program will open a Kattis Problem with its difficulty ranging from 1.3 - 4.6.

### katOpen
This program will open your desired Kattis problem based on its problem ID.