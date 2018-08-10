import sys
import csv
from msds510.utils.util import transform_record
#Importing sys which contain command-line arguments passed to the script
#Importing csv to use DictReader and DictWriter
#Importing function transform_record to be used in this program

def main():
    print(sys.argv)
    with open(sys.argv[1], 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
    # Opening the file through the command-line with DictReader that will read data as a dictionary,
    # using the header row as keys and the other rows as values

        rows = [r for r in reader]
    # List comprehension shorthand for:
        # for r in rows:
            # reader.append(r)

    # Clean fieldnames to be Python friendly
    header = rows[0]
    # Declaring "header" as the top row

    fieldnames = []
    # Creating a list named fieldnames to be appended later and used as the fieldnames for DictWriter


    for name in header:
        # Using a for loop to iterate through the header

        new_name = name.lower()
        # Making everything lowercase

        new_name = new_name.strip('\n').strip('?')
        # Removing any question marks and "\n"

        new_name = new_name.replace('/', '_').replace(' ', '_')
        # Replacing "/" and empty spaces with underscores

        fieldnames.append(new_name)
        # Appending the list fieldnames to include the modified data


    fieldnames.append('month_joined')
    # Adding new fieldnames month_joined


    # Create a new list of dictionaries with the Python friendly fieldnames
    records = []
    for row in rows:
        dictionary = {}
        for field, value in zip(fieldnames, row.values()):
            dictionary[field] = value
        records.append(transform_record(dictionary))
        # Running function transform_record on dictionary and appending result to records

    # Write to new csv file
    with open(sys.argv[2], 'w+', newline='', encoding='utf-8') as csv_file:
        w = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # opening CSV file encoded in utf-8 with write ability using DictWriter with the fieldnames argument equal to the
        # list previously created with the same name

        w.writeheader()
        # writing the headers

        w.writerows(records)
        # writing the rows as the list of dictionaries previously created named records

if __name__ == '__main__':
    main()
