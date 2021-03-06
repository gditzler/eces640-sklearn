#!/usr/bin/env python 
import utils
import bmu
import pickle 
import numpy
from sklearn import manifold
from matplotlib import pyplot as plt

# what phenotypes do we want to use?
phenotype = "COMMON_SAMPLE_SITE"

# set the paths to the mapping and biom files
biom_fp = "../data/study_550_closed_reference_otu_table.biom"
map_fp = "../data/study_550_mapping_file.txt"

# load the biom and mapping files
print "Loading the data..."
data, sample_ids, otus_names = bmu.load_biom(biom_fp)
meta_data = bmu.load_map(map_fp)
phenotype_ids = utils.return_phenotypes(sample_ids, meta_data, phenotype)

i_subset = numpy.where(phenotype_ids=="gut")

# compute the distance matrix using the hellinger divergence
print "Loading distances..."
dist_mat = pickle.load(open("../data/distances_study_500.pkl", "rb"))
 
# perform mutli-dimensional scaling
print "Running MDS..."
mds = manifold.MDS(n_components=2, max_iter=300, eps=1e-9, random_state=1, 
     dissimilarity="precomputed", n_jobs=4)
pos = mds.fit(dist_mat).embedding_

# create a 2D plot of the results
print "Making plots..."
fig = plt.figure(1)
colors = ['r','b','k','m']
 
for i,site in enumerate(numpy.unique(phenotype_ids)):
  subset = numpy.where(phenotype_ids == site)
  plt.scatter(pos[subset, 0], pos[subset, 1], s=20, c=colors[i])

plt.legend(tuple(numpy.unique(phenotype_ids)), loc='best')
plt.show()

