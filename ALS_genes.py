import bioparser.data
import os
import csv

# DOID:332 amyotrophic lateral sclerosis

def get_gwas_catalog_annotations():
    # Load gwas_catalog and gene annotations.
    gwas_catalog = bioparser.data.Data().gwas_catalog
    node_to_genes = gwas_catalog.get_doid_id_to_genes(p_cutoff=None, fdr_cutoff=None, mapped_term_cutoff=1, exclude_pmids=set())
    return node_to_genes

def get_omim_annotations():
    morbid_map = bioparser.data.Data().morbid_map
    omim_associations = morbid_map.get_associations()
    mim_to_genes = dict()
    for omim_association in omim_associations:
        mim = omim_association['mim_number']
        gene = omim_association['gene']
        mim_to_genes.setdefault(mim, set()).add(gene)

    doid = bioparser.data.Data().doid
    doid_to_xrefs = doid.get_doid_to_xrefs('OMIM')
    node_to_genes = dict()
    for doid_code, mims in doid_to_xrefs.iteritems():
        genes = set()
        for mim in mims:
            genes |= mim_to_genes.get(mim, set())
        if not genes:
            continue
        node_to_genes[doid_code] = genes
    return node_to_genes

omim_dict = get_omim_annotations()
gwas_dict = get_gwas_catalog_annotations()
doid_code = 'DOID:332'

path = "/Users/mtchavez/Documents/ALS/Diseasome/ALS-genes.txt"
write_file = open(path, 'w')
writer = csv.writer(write_file, delimiter='\t')
writer.writerow(['symbol', 'entrez', 'source'])

for gene_dict, source in [(omim_dict, 'OMIM'), (gwas_dict, 'GWAS')]:
    for gene in gene_dict[doid_code]:
        writer.writerow([gene.symbol, gene.entrez_id, source])
write_file.close()

