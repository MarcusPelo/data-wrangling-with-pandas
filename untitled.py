import os
import patoolib

path = '/mnt/Media/Torrents/completed/tv'
list = []

for root, directories, files in os.walk(path, topdown=False):
	for name in files:
		if name.endswith(".rar") == True and name.startswith("scrubs.s05") == True:
			patoolib.extract_archive(root + "/" + name, outdir=root)
			#print(root + "/" + name)


