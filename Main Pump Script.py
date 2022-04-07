import tkinter
import pandas as pd
import numpy as np
import csv
import os.path
import BasicSystemInformationSaving as BSI
from Tools.scripts.dutree import display

OpeningStatement = "Hello there, this program will help with fluids calculations"
print(OpeningStatement,'\n',"Prepare to enter some basic system information")

pumpType = float(input("What type of a pump do you have? (1 = Fixed Displacement, 2 = Variable Displacement): "))
lineNumber = float(input("How many different lines do you have?: "))

BSI.insert(pumpType, lineNumber)