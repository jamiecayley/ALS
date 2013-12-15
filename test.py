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
