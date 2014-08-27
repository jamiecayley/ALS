import csv
import math
import networkx as nx
import numpy as np
import itertools
import urllib2
from xml.dom import minidom
import pylab as plt
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
        self.diseasesInNetwork = []


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
            computed_associations[diseaseName] = self.computeNetwork(targetDisease, diseaseName)
        return computed_associations

    def computeNetwork(self, disease1):
        associatedGenes = self.diseases2genes[disease1]
        self.diseasesInNetwork.append(disease1)
        genes1 = self.diseases2genes[disease1]
        for disease2 in self.diseases2genes:
            genes2 = self.diseases2genes[disease2]
            sizeOverlap = len(genes1.intersection(genes2))
            sizeUnion = len(genes1.union(genes2))
            percentage = float(sizeOverlap) / sizeUnion
            if percentage > 0.0: 
                self.diseasesInNetwork.append(disease2)

    def computePercentageOverlap(self, disease1, disease2):
        genes1 = self.diseases2genes[disease1]
        genes2 = self.diseases2genes[disease2]
        sizeOverlap = len(genes1.intersection(genes2))
        sizeUnion = len(genes1.union(genes2))
        percentage = float(sizeOverlap) / sizeUnion
        if percentage > 0.0: 
            print disease1, disease2, percentage
            if percentage < 1.0:
                self.graph.add_edge(disease1, disease2, weight = percentage)

def main():
    fileName = "/Users/mtchavez/Documents/ALS/Diseasome/GWAS.txt" #location of GWAS catalog in computer
    path = "/users/mtchavez/Documents/ALS/Diseasome/graph2.gml" #location where you want to store gml file
    dgm = DiseaseGeneManager(fileName)
    dgm.load_data_from_csv()
    dgm.computeNetwork("Amyotrophic lateral sclerosis")     #ALS overlap with GWAS database
    for pair in itertools.product(dgm.diseasesInNetwork, repeat=2):
        dgm.computePercentageOverlap(*pair)
    pprint.pprint(dgm.graph.edges(data = True))
    dgm.computeNetwork("Schizophrenia, schizoaffective disorder or bipolar disorder")     #Schizophrenia overlap with GWAS database
    for pair in itertools.product(dgm.diseasesInNetwork, repeat=2):
        dgm.computePercentageOverlap(*pair)
    pprint.pprint(dgm.graph.edges(data = True))
    dgm.computeNetwork("Gray matter volume (schizophrenia interaction)")     #Schizophrenia overlap with GWAS database
    for pair in itertools.product(dgm.diseasesInNetwork, repeat=2):
        dgm.computePercentageOverlap(*pair)
    pprint.pprint(dgm.graph.edges(data = True))
    dgm.computeNetwork("Autism spectrum disorder, attention deficit-hyperactivity disorder, bipolar disorder, major depressive disorder, and schizophrenia (combined)")     #Schizophrenia overlap with GWAS database
    for pair in itertools.product(dgm.diseasesInNetwork, repeat=2):
        dgm.computePercentageOverlap(*pair)
    pprint.pprint(dgm.graph.edges(data = True))
    nx.write_gml(dgm.graph, path) #create a gml file to open it in cytoscape

main()

