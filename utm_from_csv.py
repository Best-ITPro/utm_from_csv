'''
utm from csv
---
Created by IgorMan, 2024
'''

import os
import csv


# UTMs (!)
def umt_labels(string):
    umt_labels_list= [
        'utm_source=github',
        'utm_medium=referral',
        'utm_campaign=company24',
    ]

    labels = ''
    for utm in umt_labels_list:
        labels += utm + '&'

    # check 1St ? in GET response
    if string.find('?') == -1:
        output = string + '?' + labels
    else:
        output = string + '&' + labels

    # cut last symbol
    output = output [0: -1]
    return output

# Output files
def file_output_sav(dir_input, files, dir_output):

    for file in files:
        file_path = dir_input + os.sep + file
        file_path_output = dir_output + os.sep + file
        print(file_path)

        # input file
        with open(file_path) as file_in:
            reader = csv.reader(file_in)
            # output file
            with open(file_path_output, 'w', newline='') as file_out:
                writer = csv.writer(file_out)
                for row in reader:
                    # exclude empty strings
                    if len(row) > 0:
                        print(umt_labels(row[0]))
                        writer.writerow([umt_labels(row[0])])

# Check dir exists
def dir_check(dir):
    if os.path.isdir(dir):
        print(f'Directory {dir} exists')
    else:
        print(f'Directory {dir} does not exist')
        print(f'Creating dir: {dir}')
        os.mkdir(dir)
        dir_check(dir)

# Files list
def files_input_list(dir):
    files = []
    dir_check(dir)
    files += os.listdir(dir)
    print(f'Files input: {files}')
    return files




# Main function
def main():
    # Settings
    current_path = os.path.dirname(__file__)
    sep = os.sep
    dir_input = current_path + sep + 'input'
    dir_output = current_path + sep + 'output'

    # Checking
    print(f'dir_input: {dir_input}')
    dir_check(dir_input)
    print(f'dir_output: {dir_output}')
    dir_check(dir_output)

    # Files List
    files_input = []
    files_output = []
    files_input = files_input_list(dir_input)


    # Get output files
    file_output_sav(dir_input, files_input, dir_output)












if __name__ == '__main__':
    main()