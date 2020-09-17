import sys
import re
import pandas as pd
import gffutils
import os

def ensg2hugo():
    
    #predifine csvFile
    csvFile = ""
    
    # check if column option
    if len(sys.argv) > 2:
        if sys.argv[1][:2] == "-f":
        #if ture, get the column number, but it need to minus 1 becasue of index
            colNumber = int(sys.argv[1][2]) - 1
        #redifine  csvFile
            csvFile = sys.argv[2]
    else:
        #if there is no '-f' argument, pick the first column(for index, should be 0)
        colNumber = 0
        #redifine  csvFile
        csvFile = sys.argv[1]
        
    # data = pd.read_csv("expression_analysis.csv", index_col=0)
    
    #check exist homo_sapiens gtf database or not
    if os.path.isfile('Homo_sapiens.db') != True:
        #if not exist, create new db through "gtf library"
        db = gffutils.create_db(
            'Homo_sapiens.GRCh37.75.gtf',
            dbfn='Homo_sapiens.db',
            verbose=True,
            merge_strategy='error',
            disable_infer_transcripts=True,
            disable_infer_genes=True,
        )
    
    #make a dictionary to lookup gene_name
    ensgGeneName = {}
    db = gffutils.FeatureDB('Homo_sapiens.db')
    #through each line to get the gene_id and gene_name
    for f in db.all_features():
        #convert list to string
        gene_ID = ''.join(f['gene_id'])

        gene_NAME = ''.join(f['gene_name'])

        ensgGeneName[gene_ID] = gene_NAME

    #read each line and append them into a list
    listLines = []
    #open the csvfile
    with open(csvFile, 'r') as file:
        #since the first line is header, skip it
        first_line = file.readline()
        listLines.append(first_line)
        #from line to line in the file
        for line in file:
            #split this line into list
            lineList = line.split(",")
            #use regex expression to get gene_id without .decimal 
            #since user pick colNumber or automical pick first column
            match = re.match(r'\"(\w*).\w*\"', lineList[colNumber])
            if match:
                geneID = match.group(1)
                #look up the gene_id in the dictionary or not
                if ensgGeneName.get(geneID) is not None:
                    #if exist, replace with gene_name
                    lineList[colNumber] = '"' + ensgGeneName[geneID] + '"'
                else:
                    #if not exist, input unknown
                    lineList[colNumber] = '"UnKnown"'
            else:
                print("no match")
            #append to the huge list
            listLines.append(lineList)
    
    #print out each line in the listLines
    print(listLines[0])
    for i in range(1, len(listLines)):
        eachLine = ', '.join([str(elem) for elem in listLines[i]]) 
        print(eachLine)
    
    
    #Use Pandas
    # # ensgGeneName = ensgName()
    # ensg = data["gene_id"]
    # ensgList = list(ensg)
    # for i in ensgList:
    #     match = re.match(r'(\w*).\w*', i)
    #     if match:
    #         geneId = match.group(1)
    #         # print(geneId)
    #         # print(ensgGeneName[geneId])
    #         # print(i)
    #         # geneName = db[str(geneId)].attributes['gene_name']
    #         data["gene_id"].replace({i:geneId}, inplace=True)
    #     else:
                   
    #         print("No match!!!")
    # data['gene_id'] = data['gene_id'].map(ensgGeneName)
    
    # dataNew = data.rename(columns={'gene_id': 'gene_name'})

    # print(dataNew.head(10))



ensg2hugo()
