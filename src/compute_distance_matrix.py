#!/usr/bin/env python
import utils
import bmu
import pickle

# set the paths to the mapping and biom files
biom_fp = "../data/study_550_closed_reference_otu_table.biom"
map_fp = "../data/study_550_mapping_file.txt"

data, sample_ids, otus_names = bmu.load_biom(biom_fp)
dist_mat = utils.compute_distance_matrix(data)
pickle.dump(dist_matrix, open("../data/distances_study_500.pkl", "wb"))
