# didactic-tribble
Leading Causes of Death

Process an xml file by using the ElementTree libraries. In addition to the module videos, also use the ElementTree online tutorial as reference:

https://docs.python.org/3.4/library/xml.etree.elementtree.html (Links to an external site.)
Objectives
This assignment will give you the opportunity to:

Use the ElementTree XML to move data from one format (XML) to another (Python dictionary)
Understand the differences between XML attributes and XML elements
Process a large data file that could not be done by hand.
Assignment Instructions
To complete this assignment follow these steps:

Download the leading_causes_of_death.xml  Download leading_causes_of_death.xmlfile. This file contains the leading of causes of death for each state during the last 20 years. (You may need to right click the link and select 'Save Link As...' in order to download the file).
Write a python script to process the data in the xml.
At the first of the file (after any import statements) define three functions
main()
process_row(row)
print_rows(row_list)
In the main function:
Ask the user to input a year ("Please enter a year: ")
An empty list variable called cod_list should be initialized
A for loop should be used to move through the row elements of the xml file.
Each row in the xml file should be passed to the process_row function. The process_row function should return a dictionary. Each dictionary should then be appended to the cod_list
After the for loop the cod_list should be passed to the print_rows function
Also pass the inputted year as a parameter to the print_rows function
In the print_rows function
A for loop to move through each dictionary using the enumerate function to keep track of the index
If the year matches the user inputted year, print out the record index, the id of the row, and the informational text that follows this pattern:
Record 2 (id: 15031): During 2016 the leading cause of death in Arizona was Unintentional Injuries
Within the process_rows function:
Every element in a row should become a key-value pair (example: 'year', 'state', and 'deaths' are all examples of keys and the associated text would be their values within the dictionary)
Also, each dictionary item should also include a key-value pair specifying the id of the row.
Code minimalism requirements:
You should use the if __name__=='__main__':  syntax to call your main method
Do not use global variables. If a function needs a variable then pass it as a parameter.
The only code at the far left indent should be functions, import statements, and the if statement that calls the main function
Do not use inner functions (a function within a function)
Submit your final python script as the assignment
