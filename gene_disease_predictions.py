from scipy import stats
import itertools
import pprint
import networkx as nx
import csv

class DiseaseGeneManager:
  def __init__(self, fileName):
    self.fileName = fileName
    self.disease2genes = {}
    #Maps from diseaseName::String to{geneProbability::string}
    self.graph = nx.Graph()
    #creates a networkx graph
    self.diseases = []

  def load_data_from_csv(self):
    read_file = open(self.fileName)
    reader = csv.reader(read_file, delimiter = '\t')
    fieldnames = reader.next()
    self.diseases = fieldnames[1:]

  def calculate_correlation(self, disease1, disease2):
      correlation = scipy.stats.spearmanr(disease1, disease2)
      self.graph.add_edge(disease1, disease2, weight = correlation)
      write_file = open('disease_predictions.csv', wb)
      writer = csv.writer(write_file, delimiter = '\t')
      writer.writerow(("disease 1", "disease 2", "correlation"))
      writer.writerow((disease1, disease2, correlation))

def main():
  fileName = '/Users/mtchavez/Downloads/prediction-table.txt'
  path = '/Users/mtchavez/documents/probabilities_graph.gml'
  dgm = DiseaseGeneManager(fileName)
  dgm.load_data_from_csv()
  for pair in itertools.product(dgm.diseases, repeat=2):
    dgm.calculate_correlation(*pair)
  pprint.pprint(dgm.graph.edges(data = True))
  nx.write_gml(dgm.graph, path)

main()
