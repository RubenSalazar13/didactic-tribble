from xml.etree import ElementTree as ET

# Parse the XML file from local machine and may have to be altered to correct path
root = ET.parse('/home/ruben/Desktop/Python/IS4485-090/Mod9/leading_causes_of_death.xml').getroot()

def main():
    # Asks the user to input year
    year = input("Please enter a year: ")
    # Empty variable
    cod_list = []
    # Iteration through the XML rows
    for row in root[0]:
    # Call the process_row() function to get the row as a dictonary
        cod_list.append(process_row(row))
    # Call the print rows() function
    print_rows(cod_list, year)

def print_rows(row_list, year):
    for data,info in enumerate(row_list):
        if info['year'] == year:
            print("Record {} (id: {}): During {} the leading cause of death in {} was {}".
                format(data, info['_id'],year,info['state'],info['cause_name']))

def process_row(row):
    # Dictonary to store key: value pairs
    glossary = {}
    glossary['_id'] = row.get('_id')

    # Iterate through each element
    for interate in row:
    # Create a dictory items
        glossary[interate.tag] = interate.text
    return glossary

if __name__=='__main__':
# Call main function
   main()

