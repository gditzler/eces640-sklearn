#!/usr/bin/env python 
import numpy
from scipy.linalg import norm
from multiprocessing import Pool

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

def hellinger(p, q):
  """
  return the hellinger distance between distributions p & q
   :q, p - probability vectors
  """
  return norm(numpy.sqrt(p) - numpy.sqrt(q))/numpy.sqrt(2.0)

def compute_distance_matrix(data):
  """
  """
  pool = Pool(2)
  n_samples = len(data)
  dist_mat = numpy.zeros([n_samples, n_samples])
  res = []

  for i in range(n_samples):
    print i
    for j in range(i+1,n_samples):
      p = data[i]/data[i].sum()
      q = data[j]/data[j].sum()
      res.append(pool.apply_async(hellinger, args=(p,q))) 
      #dist_mat[i,j] = hellinger(p, q)
  pool.close()
  pool.join()
  return dist_mat
