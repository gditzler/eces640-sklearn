#!/usr/bin/env python 
import utils
import bmu
import pickle 
from sklearn import manifold

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

# compute the distance matrix using the hellinger divergence
print "Loading distances..."
dist_mat = pickle.load(open("../data/distances_study_550.pkl", "rb"))

mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed, 
    dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_



plt.scatter(pos[:, 0], pos[:, 1], s=20, c='g')


