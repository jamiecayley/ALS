1) Assemble a list of ALS genes. (GWAS Catalog, OMIM, manual)

2) Translate genes into entrez identifiers.

3) Create a subsetted version of gene_word_matrix.gz with only the relevant genes.
Download: http://www.broadinstitute.org/mpg/grail/
fieldnames = ['entrez_id', 'word', 'average_count']
gzip package in python: gzip.open(path)

gene_word_reader(path)
use the yield statement

4) For every word in the full gene_word_matrix.gz, calculate the average average_count and the standard deviation across all genes. Save these results to a file where each row represents a word.
