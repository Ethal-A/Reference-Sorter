import sys

def sort_references(references):
    '''
    @param references: a list of references
    
    @returns list of references in sorted alphabetical order

    Ignores all non-latin characters (a-z, A-Z)
    '''

try:
    # Get parameters, (file name)
    if (len(sys.argv) < 2):
        raise Exception('Please provide a file name')
    file_name = sys.argv[1]
    file_link = open(file_name)

    # Read file contents
    content = file_link.read().split('\n')
    print(content)
except Exception as err:
    print(err)

