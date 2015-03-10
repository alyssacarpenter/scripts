#! /usr/bin/env python

import hashlib,os

def md5_for_file(f,block_size=2**20):
  md5 = hashlib.md5()
  while True:
    data = f.read(block_size)
    if not data:
      break
    md5.update(data)
  return md5.digest()

def beautify(fileListings):
  removedHead = fileListings.split("\n\n")[1:]
  directoryFiles = []
  for listing in removedHead:
    directoryFiles.append(listing.split(":"))
  for i in range(directoryFiles):
    directoryFiles[i]=directoryFiles[i][1].split("\n")
  for pair in directoryFiles:
    for file in pair[1]:
      if os.path.isfile(pair[0]+file):
