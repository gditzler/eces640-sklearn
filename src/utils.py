#!/usr/bin/env python 
import numpy

__author__ = "Gregory Ditzler"
__copyright__ = "Copyright 2014, EESI Laboratory (Drexel University)"
__credits__ = ["Gregory Ditzler"]
__license__ = "GPL"
__version__ = "0.3.0"
__maintainer__ = "Gregory Ditzler"
__email__ = "gregory.ditzler@gmail.com"
__status__ = "development"


def return_phenotypes(samples, metadata, phenotype_id):
  """
  return the phenotype labels from data stored in a mapping dictionary
   :samples - sample IDs 
   :metadata - dictionary of the metadata
   :phenotype_id - string containing the column name in the mapping file that 
     is going to be used as the determinant of the label

   RETURNS
   :label - numpy array of labels
  """
  labels = []
  for sample in samples: 
    labels.append(metadata[sample][phenotype_id])
  return numpy.array(labels)

