#!/usr/bin/env Python3

from multiprocessing import Pool
import subprocess
import os

src = "/home/student-02-0e0d51d542ae/data/prod/"
dest = "/home/student-02-0e0d51d542ae/data/prod_backup/"

def run(item):
    subprocess.call(["rsync", "-arq", src, dest])

folder = []

for path, dir, file in os.walk(src):
    folder.append(dir)

p = Pool(len(folder))
p.map(run, folder)
