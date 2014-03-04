# File Descriptions
* `bmu.py` - This module implements functions to handle biom and mapping files without installing [QIIME](http://qiime.org/) or the [BIOM](http://biom-format.org/) tools. The BIOM files are parsed as the JSON objects and the file contents are returned as a data matrix, OTU names, and sample IDs. 
* `compute_distance_matrix.py` - The `demo-mds.py` script applies MDS to biological data collected from the earth microbiome project; however, due to time contraints `demo-mds.py` does not compute the pairwise distance matrix that we need. Therefore. `compute_distance_matrix.py` was used to compute the distance matrix and I have added the pickled file to the `data/` folder. No need to run this script! Its just here for reference. 
* `demo-manifold.py` - Implement ISOMAP on the classical [swiss roll](http://isomap.stanford.edu/datasets.html) data set. Its not biological, but it serves as a good demonstration of ISOMAP's capabilities.  
* `demo-mds.py` - This script implements MDS on `study 550` from the [Earth Microbiome Project](http://www.earthmicrobiome.org/). 
* `demo-pca.py` - This script demonstrates PCA and LDA on the Fisher Iris data. 
* `README.md` - You're reading it right now!
* `utils.py` - This module contains several functions that I used several times, so I put them into a single Python file to keep the repo clean. 
