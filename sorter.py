import sys
import os
import re

def sort_references(references):
    '''
    @param references: a list of references
    
    @returns list of references in sorted alphabetical order

    Ignores all non-latin characters (sorts only bazed on a-z and A-Z)
    '''
    # Ignore all non-latin characters and sort
    references = sorted(references, key=lambda x: re.sub('[^A-Za-z]+', '', x).lower())
    return references

try:
    # Get parameters, (file name)
    if (len(sys.argv) < 2):
        raise Exception('Please provide a file name')
    file_name = sys.argv[1]
    if (not os.path.isfile(file_name)):
        raise Exception('{} is not a file in this directory'.format(file_name))
    file_link = open(file_name)

    # Read file contents
    content = file_link.read().split('\n')

    # Close link
    file_link.close()

    # Sort the content
    content = sort_references(content)

    # Open link to new 'sorted' file to write to
    split_path = os.path.splitext(file_name)
    base_name = split_path[0]
    extension = split_path[1]
    writer = open('{} (sorted){}'.format(base_name, extension), 'w')

    # Output sorted content to a file
    for ref in content:
        # Check if empty string
        if (len(ref) == 0):
            continue

        writer.write(ref + ('\n\n' if ref != content[len(content) - 1] else ''))

    # Close link
    writer.close()
except Exception as err:
    print(err)

