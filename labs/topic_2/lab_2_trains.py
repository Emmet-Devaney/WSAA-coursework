import requests 
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get (url)
doc = parseString(page. content)
# check it works
print (doc. toprettyxml()) #output to console comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

'''
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    #traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode)
    trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlatitude = trainlatitudenode.firstChild.nodeValue.strip()
    print (trainlatitude)
'''

with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
      
        print(traincode)
        
        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)


retrieveTags = ['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction']


'''
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)

        train_writer.writerow(dataList)
'''

with open('week03_train_filtered.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        # extract TrainCode first
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        # Filter for TrainCode starting with "D"
        if not traincode.startswith("D"):
            continue
        
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            #avoid errors if a tag is missing
            if datanode and datanode.firstChild:
                dataList.append(datanode.firstChild.nodeValue.strip())
            else:
                dataList.append("N/A")
        train_writer.writerow(dataList)
