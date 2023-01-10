import re
import requests
proteins = []
with open(r"C:\Users\robin\Downloads\rosalind_mprt (3).txt") as fp:
    for lines in fp:
        proteins.append(lines.replace('\n',''))


for i in proteins:
    res = []
    res.append(i)
    if '_' in i:
        i = i.split('_')[0]

    seq = ''
    url = 'http://www.uniprot.org/uniprot/' + i + '.fasta'
    response = requests.get(url=url).text
    index_pos = response.find('\nM')
    seq+=response[index_pos:].replace('\n','')
    find = re.compile(r'N(?=[^p][ST][^P])')
    f = re.finditer(find,seq)
    for _ in f:
        res.append(str(_.span()[1]))
    if len(res)>1:
        print(res[0])
        print(' '.join(res[1:]))