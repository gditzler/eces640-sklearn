# Obtaining the data

The data was download from the [Earth Microbiome Project](http://www.earthmicrobiome.org/) on 11/1/2013. In particular, we are interested in the [Caporaso Illumina time series study](ftp://thebeast.colorado.edu/pub/QIIME_DB_Public_Studies/study_550_split_library_seqs_and_mapping.zip). I have not changed the files. I downloaded the data and extracted the `biom` and `mapping` files for this demo. The original download on the EMP website has the sequence data, which is not needed for what we wish to demonstrate. 


# About the Files
* `distances_study_500.pkl` - Pickled distance matrix for study 550. The distance between samples is computed using the [Hellinger distance](http://www.tcs.tifr.res.in/~prahladh/teaching/2011-12/comm/lectures/l12.pdf) 
* `distances_study_500.pkl.gz` - Compressed version of `distances_study_500.pkl`
* `study_550_closed_reference_otu_table.biom` - study 550's BIOM file
* `study_550_mapping_file.txt` - study 550's mapping file containing the metadata

