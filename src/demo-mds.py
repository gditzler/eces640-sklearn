#!/usr/bin/env python 
import utils
import bmu

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
print "Computing distances..."
dist_mat = utils.compute_distance_matrix(data)
