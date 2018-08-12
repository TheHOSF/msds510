import sys
import csv
import msds510
#Importing sys which contain command-line arguments passed to the script
#Importing csv to use DictReader
#Importing function top_ten_appearance_records to be used in this program

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


    with open(sys.argv[2], 'w+', newline='') as md:
        for record in msds510.top_ten_appearance_records(rows):
            # iterating through file using function top_ten_appearence_records

            md.writelines(record)
            # writing markdown report


if __name__ == '__main__':
    main()
