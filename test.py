import csv
import math
import networkx as nx
import numpy as np

path = '/Users/mtchavez/Documents/ALS/Diseasome/GWAS.txt'
read_file = open(path)
reader = csv.reader(read_file, delimiter = '\t')
fieldnames = reader.next()

rows = list(reader)
read_file.close()

write_file = open('datatest.csv', 'wb')
writer = csv.writer(write_file, delimiter = '\t')
writer.writerow(('disease', 'genes'))

disease_gene = dict()
for row in rows:
    if not row:
            continue
    disease = row[7]
    for x in row:
        reported_genes = row[13]
        if reported_genes == 'NR':
            reported_genes = row[14]
        if reported_genes == 'Intergenic':
            reported_genes = row[14]

    if reported_genes == ' - ' or \
      reported_genes == 'Pending':
        continue

    reported_genes = set(reported_genes.split(','))
    group = disease_gene.setdefault(disease, [])
    for x in reported_genes:
       group.append(x)

    writer.writerow((disease, reported_genes))

print disease_gene['Amyotrophic lateral sclerosis']

write_file.close()

def intersect(a, b):
    return set(set(a) & set(b))

def num_elems(x):
    return sum(1 for elem in x if elem)

def shared_genes(disease, data):
    num1 = num_elems(disease)
    for x in data:
        print x
        num2 = num_elems(x)
        common_genes = intersect(disease, x)
        if num_elems(common_genes) == 0:
            print "No shared genes"
        else:
            percentage_common = num_elems(common_genes)/(num1 + num2)
            print percentage_common
        
print shared_genes(disease_gene['Amyotrophic lateral sclerosis'], disease_gene)


