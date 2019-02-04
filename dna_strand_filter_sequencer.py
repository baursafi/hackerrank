#!/usr/bin/python

'''
Was taking a short test on HackerRank and the task was to filter given set of DNA strands by the following conditions:
- strand has to be longer than 10 characters
- strand has to be shorter than 100 characters
- should only contain capital letters
- strand should only consist of A, C, T, G letters
- if the resulting list has less than 3 elements, than return an empty string.

Part 2 required to sequence each strand in the filtered sequence by matching the last and the first three letters
of each strand, then joining such matching strands and removing the overlapping endings.

Part 3 required to match every three elements to an aminoacid, and the dictionary was supposed to be provided by
a variable inside the code. I will skip this part as I don't have such vocabulary.
'''
# This function filters the strands that satisfy a list of conditions
def strandfilter(strandlist):
    outputlist = []
    for strand in strandlist:
        if (len(strand) > 10) and (len(strand) < 100) and (set(strand) <= set('ACTG')):
            outputlist.append(strand)
    if len(outputlist) < 3:
        return ''
    else:
        return outputlist
# The next function sequences the strands and builds an DNA sequence overlapping the first
# and the last three aminoacids removing the overalps

def strandsequencer(samplist):
    element = ''

    while samplist:
        if element == '':
            element = samplist[0]
            del samplist[0]

        j = 0
        while samplist:

            if element[-3:] == samplist[j][:3]:
                element = element[:-3] + samplist[j]
                del samplist[j]

            elif element[:3] == samplist[j][-3:]:
                element = samplist[j] + element[3:]
                del samplist[j]


    return element

#To make sure it works let's try a trylist
li = ['AGTGGGGGGGA', 'CTAGACT', 'GGAAACCCAATTT', 'GACTTLLKJSGGC', 'TTTGGCAGCTAGT', 'GCTGGGCCGGCAGT']

samplist = strandfilter(li)
print('Filtered list of strands: ', samplist)

newlist = strandsequencer(samplist)
print('Final strand compilation with overlaps removed: ', newlist)
