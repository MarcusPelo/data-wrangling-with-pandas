#!/usr/bin/python

import pandas as pd
import os
import patoolib as ptl
import numpy as np

mediaPath = '/Volumes/Downloads/Games/Games'
mediaType = 2 #input("Qual tipo de media deseja analisar?\n1. TV \n2. Files")
mediaDF = pd.DataFrame()
mediaFolder = pd.DataFrame()
mediaDict = {}
mediaList = [['0','0','0']]
mediaFolderList = []
c = 1

# function to get unique values
def unique(list1):
    x = np.array(list1)
    print(np.unique(x))

# if int(mediaType) == 2:
#     mediaPath = mediaPath + "tv"

for root, directories, files in os.walk(mediaPath, topdown=False):
    for name in files:
        if name.endswith('.rar') == True: 
            flg = 0 
        else:
            flg = 1
        mediaList.insert(c,[root, name, flg])
        c = c + 1


# Convertendo lista em dataframe
mediaDF = mediaDF.append(mediaList,ignore_index=True)

# add colunas ao df      
mediaDF.columns = ['parentFolder', 'fileName', 'flgDelete']



mediaFolder = pd.DataFrame(mediaDF.parentFolder.unique())
mediaFolder.columns = ['parentFolder']
mediaFolder = mediaFolder.drop([0])

mediaFolder = mediaFolder.sort_values(by=['parentFolder'])
mediaFolder = mediaFolder.reset_index(drop=True).drop([0])

mediaFolder.head()

print("Qual pasta deseja acessar? \n")
print(mediaFolder)

# mediaFolder = mediaDF.parentFolder.unique()

# mediaFolder = mediaDF.append(mediaFolder,ignore_index=True)
#mediaFolder.head(100)


# mediaDF_rar = mediaDF[mediaDF["fileName"].str.lower().str.endswith('.rar')]
# mediaDF_r00 = mediaDF[mediaDF["fileName"].str.lower().str.endswith('.r00')]
# mediaFlg = mediaDF[mediaDF.flgDelete.eq(1)]
# mediaDop = mediaDF[mediaDF.parentFolder.str.contains('Dopesick', case=False)]
# mediaScr = mediaDF[mediaDF.parentFolder.str.contains('scrubs', case=False)]
# mediaDF = mediaDF[~mediaDF.parentFolder.isin(mediaFlg.parentFolder)]
# mediaDF = mediaDF[~mediaDF.parentFolder.isin(mediaDop.parentFolder)]
# mediaDF = mediaDF[~mediaDF.parentFolder.isin(mediaScr.parentFolder)]

# mediaDF_rar = mediaDF[mediaDF["fileName"].str.lower().str.endswith('.rar')].sort_values(by=['parentFolder'])
# mediaDF_rar.to_csv('/mnt/Media/media.csv')
#mediaDF.head(100)