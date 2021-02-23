import sys
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
    file_link = open(file_name)

    # Read file contents
    content = file_link.read().split('\n')
    print(sort_references(content))
except Exception as err:
    print(err)

