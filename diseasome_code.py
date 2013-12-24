import csv
import math
import networkx as nx
import numpy as np
import itertools
import pprint

class DiseaseGeneManager:
    def __init__(self, fileName):
        self.fileName = fileName
        self.genes2diseases = {}
        # Maps from geneName::String to {diseaseName::string}
        self.diseases2genes = {}
        # Maps from diseaseName::String to {geneName::string}
        self.graph = nx.Graph()
        # Creates a networkx graph


    def load_data_from_csv(self):
        read_file = open(self.fileName)
        reader = csv.reader(read_file, delimiter='\t')
        fieldnames = reader.next()
        for row in reader:
            if not row:
                continue
            diseaseName = row[7]
            reported_genes = row[13]
            if reported_genes == 'NR' or reported_genes == 'Intergenic':
                reported_genes == row[14]

            if reported_genes == ' - ' or reported_genes == 'Pending':
                continue

            reported_genes = set(reported_genes.split(','))
            group = self.diseases2genes.setdefault(diseaseName, set())

            group.update(reported_genes)
        read_file.close()


    def computeSharedGenes(self, targetDisease):
        associatedGenes = self.diseases2genes[targetDisease]
        computed_associations = {} # map from diseaseName to percentage overlap with targetDisease
        for diseaseName in self.diseases2genes:
            computed_associations[diseaseName] = self.computePercentageOverlap(targetDisease, diseaseName)
        return computed_associations

    def computePercentageOverlap(self, disease1, disease2):
        genes1 = self.diseases2genes[disease1]
        genes2 = self.diseases2genes[disease2]
        sizeOverlap = len(genes1.intersection(genes2))
        sizeUnion = len(genes1.union(genes2))
        percentage = float(sizeOverlap) / sizeUnion
        print disease1, disease2, percentage
        if percentage > 0.0: 
            #self.graph.add_node(disease2)
            self.graph.add_edge(disease1, disease2, weight = percentage)

    def egoGraph(self, targetDisease):
        ego = targetDisease
        nodes = set([ego])
        nodes.update(self.graph.neighbors(ego))
        egonet = self.graph.subgraph(nodes)
    
def main():
    fileName = "/Users/mtchavez/Documents/ALS/Diseasome/GWAS.txt" #location of GWAS catalog in computer
    path = "/users/mtchavez/Documents/ALS/Diseasome/graph.gml" #location where you want to store graph
    dgm = DiseaseGeneManager(fileName)
    dgm.load_data_from_csv()
    dgm.computeSharedGenes("Amyotrophic lateral sclerosis")     #ALS overlap with GWAS database
    #dgm.egoGraph('Amyotrophic lateral sclerosis')
    pprint.pprint(dgm.graph.edges(data = True))
    nx.write_gml(dgm.graph, path)
    '''inflamatory_diseases_1 = ["Crohn's disease", "Ulcerative colitis", "Rheumatoid arthritis", "Systemic lupus erythematosus", "Type 1 diabetes", "IgA nephropathy", "Multiple sclerosis", "Vitiligo", "Psoriasis", "Atopic dermatitis", "Ankylosing spondylitis", "Celiac disease", "Primary biliary cirrhosis", "Systemic sclerosis", "Primary sclerosing cholangitis"]
    for pair in itertools.product(inflamatory_diseases_1, repeat=2):
        dgm.computePercentageOverlap(*pair)     #replication of a study by Cotsapas and Hafler (2013)'''


main()

