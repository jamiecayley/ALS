#ALS Diseasome

##Goal:

Construct a human disease network (diseasome) for ALS (amyotrophic lateral sclerosis)
In the network, each node is a disease and edges represent shared succeptible genes. 

##Methods: 

 In order to create a diseasome, a larger network of diseases (nodes) connected to genes (edges) is created first, where connections (edges) come from the GWAS catalog (reference), and the OMIM database (reference). The Disease Ontology (DO) (reference) is used to provide a standardized terminology for disease concepts across both resources. Two processing steps are performed on the resulting network of DO terms annotated with associated genes: (1) closely related concepts are merged by transferring annotations to a single term and removing the other term (for example ‘breast cancer’ is consolidated with ‘breast carcinoma’); and (2) terms of inappropriate generality are removed such as ‘immune system disease’. 
 
Each gene receives a weight equal to the inverse of the square root of its frequency. The edge weight between diseases in the network is calculated as the sum of the weights for the intersection of genes divided by the sum of weights for the union of genes. Edges between diseases with no shared genes are omitted. 

###Random Walk with restart:
To determine proximity of a node to any other node in the network a random walk with restart can be used. The disease of interest (ALS) is masked from the network, the corresponding edge weights are used as seed probabilities for a random walk with a restart probability of 0.2 at each step which is run until convergence.

