# Refernece-Sorter
Reference-Sorter is a python script which sorts a list of references for the user in a line by line order.

## Usage
Simply create file containing the list of references (empty spaces will be ignored). For this example, the file will be called 'references.txt'. Please note that any there should be no new lines inside a single reference. There may be however, a new line between references.

The following should work:
```
Barnett, D., 2018, Can we trust Wikipedia? 1.4 billion people can't be wrong, Independent, viewed 23 Feb 2021, https://www.independent.co.uk/news/long_reads/wikipedia-explained-what-it-trustworthy-how-work-wikimedia-2030-a8213446.html

Wikipedia, n.d., Wikipedia:Wikipedia is not a reliable source, viewed 23 Feb 2021, https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_is_not_a_reliable_source
```

The following will **NOT** work (new line for the references):
```
Barnett, D., 2018, Can we trust Wikipedia? 1.4 billion people can't be wrong, Independent, viewed 23 Feb 2021,
https://www.independent.co.uk/news/long_reads/wikipedia-explained-what-it-trustworthy-how-work-wikimedia-2030-a8213446.html

Wikipedia, n.d., Wikipedia:Wikipedia is not a reliable source, viewed 23 Feb 2021,
https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_is_not_a_reliable_source
```

To sort the references simply use the command:
`python3 sorter references.txt`

The script will output a file called 'references (sorted).txt' which contains a sorted list of the provided references.