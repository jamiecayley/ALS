import csv
import math
import networkx as nx
import numpy as np

class DiseaseGeneManager:
    def __init__(self, fileName):
        self.genes2diseases = {}
        # Maps from geneName::String to {diseaseName::string}
        self.diseases2genes = {}
        # Maps from diseaseName::String to {geneName::string}
        tabularData = elf.load_data_from_csv(fileName)
        self.process_data(tabularData)


    def load_data_from_csv(self, csvFileName):
        #do something
        with open(csvFileName, 'rb', delimeter = '\t') as fileInput:
            fieldnames = csv.reader.next()
            for row in csv.reader(fileInput):
                if not row:
                    continue
                diseaseName = row[7]
                reported_genes = row[13]
                if reported_genes == 'NR' or reported_genes == 'Intergenic':
                    reported_genes == row[14]

                if reported_genes == ' - ' or reported_genes == 'Pending':
                    continue

                reported_genes = set(reported_genes.split(','))
                group = diseases2genes.setdefault(disease, set())

                group.update(reported_genes)

        self.

    def computeSharedGenes(self, targetDisease):
        associatedGenes = self.diseases2genes[targetDisease]
        computed_associations = {} # map from diseaseName to percentage overlap with targetDisease
        for diseaseName in self.diseases2genes:
            computed_associations[diseaseName] = self.computePercentageOverlap(targetDisease, diseaseName)
        return computed_associations

    def computePercentageOverlap(self, disease1, disease2):
        genes1 = self.diseases2genes[disease1]
        genes2 = self.diseases2genes[disease2]
        sizeOverlap = len(genes1.intersect(genes2))
        sizeUnion = len(genes1) + lens(genes2)
        percentage = sizeOverlap / sizeUnion
        return percentage

def main():
    fileName = "/Users/mtchavez/Documents/ALS/Diseasome/GWAS.txt"
    dgm = DiseaseGeneManager(fileName)
    print dgm.computeSharedGenes("Amyotrophic lateral sclerosis")
