import csv

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
	disease = row[7]
	reported_genes = row[13]
	if reported_genes == 'NR':
		reported_genes = row[14]
	if reported_genes == 'Intergenic':
		reported_genes = row[14]
	disease_gene[disease] = reported_genes
	writer.writerow((disease, reported_gene))

print disease_gene
print disease_gene['Amyotrophic lateral sclerosis']


write_file.close() 
