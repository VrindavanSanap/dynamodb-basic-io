import requests
import gzip
import os
import hashlib
import numpy as np
from tqdm import tqdm
from putdata_into_db import add_data

def fetch(url):

  fp = os.path.join("/tmp", hashlib.md5(url.encode('utf-8')).hexdigest())
  if os.path.isfile(fp):
    with open(fp, "rb") as f:
      dat = f.read()
  else:
    with open(fp, "wb") as f:
      dat = requests.get(url).content
      f.write(dat)
  return np.frombuffer(gzip.decompress(dat), dtype=np.uint8).copy()


X_train = fetch(
    "https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz")[0x10:].reshape((-1, 28 * 28))
Y_train = fetch(
    "https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz")[8:]
X_test = fetch(
    "https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz")[0x10:].reshape((-1, 28* 28))
Y_test = fetch(
    "https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz")[8:]

def add_data_( ):
    for index in tqdm(range(X_train.shape[0])):
        add_data("train", index, X_train[index].tolist(), Y_train[index].tolist())



add_data_()
