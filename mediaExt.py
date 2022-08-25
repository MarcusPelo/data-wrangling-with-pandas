#! /usr/bin/python

import pandas as pd
import os
import patoolib as ptl


mediaPath = '/mnt/Media/Torrents/completed/'
mediaType = 2 #input("Qual tipo de media deseja analisar?\n1. TV \n2. Files")
mediaDF = pd.DataFrame()
mediaDict = {}
mediaList = [['0','0','0']]
c = 1

if int(mediaType) == 2:
    mediaPath = mediaPath + "tv"

    for root, directories, files in os.walk(mediaPath, topdown=False):
        for name in files:
            if name.endswith('.mkv') == True: 
                flg = 1 
            else:
                flg = 0
            mediaList.insert(c,[root, name, flg])
            c = c + 1


mediaDF = mediaDF.append(mediaList,ignore_index=True)      
mediaDF.columns = ['parentFolder', 'fileName', 'flgDelete']

mediaDF_rar = mediaDF[mediaDF["fileName"].str.lower().str.endswith('.rar')]
mediaDF_r00 = mediaDF[mediaDF["fileName"].str.lower().str.endswith('.r00')]
mediaFlg = mediaDF[mediaDF.flgDelete.eq(1)]
mediaDop = mediaDF[mediaDF.parentFolder.str.contains('Dopesick', case=False)]
mediaDF = mediaDF[~mediaDF.parentFolder.isin(mediaFlg.parentFolder)]
mediaDF = mediaDF[~mediaDF.parentFolder.isin(mediaDop.parentFolder)]

mediaDF_rar = mediaDF[mediaDF["fileName"].str.lower().str.endswith('.rar')].sort_values(by=['parentFolder'])
mediaDF_rar.to_csv('/mnt/Media/media.csv')



#mediaDF.head(100)

# iterate through each row and select
# 'Name' and 'Stream' column respectively.
mediaDF_rar = mediaDF_rar.head(10)

for ind in mediaDF_rar.index:
    file = mediaDF_rar['parentFolder'][ind] + '/' + mediaDF_rar['fileName'][ind]
    print("Extracting file " + mediaDF_rar['parentFolder'][ind] + '/' + mediaDF_rar['fileName'][ind])
    ptl.extract_archive(file, outdir=mediaDF_rar['parentFolder'][ind])
    print("End of extraction")
    # print(mediaDF_rar['parentFolder'][ind], mediaDF_rar['fileName'][ind])
