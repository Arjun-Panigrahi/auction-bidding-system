#Imports
import os
os.system("pip install firebase-admin")
# import random
from datetime import datetime # import time
import firebase_admin
from firebase_admin import credentials, firestore
#JSON File & it's Path
#FilePath = "C:\\Users\\ACER\\Downloads\\Arjun\\serviceAccountKey.json" #auction-bidding-arjun-gupta-firebase-adminsdk-mdv94-337a016199.json
jsonWriter = open("serviceAccountKey.json","w+")
jsonWriter.write('{\n')
jsonWriter.write('  '+'"type": "service_account",\n')
jsonWriter.write('  '+'"project_id": "auction-bidding-arjun-gupta",\n')
jsonWriter.write('  '+'"private_key_id": "337a0161999584d4f5bb4f520f960a5ec63ba961",\n')
jsonWriter.write('  '+'"private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyB7LNuG7apTjm\\nTSYmZlXrb1OOBau38lZwLoZkB9Z+mWfYpGfEIywAj9MiCWPRQZpywC3EpiX1zFOP\\neXaBa4P46X+T5kRIyq4MsAdg5HO3iP6o0YrtFsBn7Ij+qypfvs4xpzSQ4Jj7VHxr\\nKsyXRoWxA9tYEpqIR0N++KqPVSlk0bBDUBws+DvH2rymG1lyuSxScHOiLY6ZUX8z\\n7BFY1/GpYjPq0CaAYB4nqyV6Qg2AXivWnK8bEkEdoVGzrpWYilmfTdiVXg6Zwj/o\\njT2+V69CYvq6IkKFfUdje0Bgw+CamU0Ws1insoFyiwObuOIpMEt23gHEGPMn1cIX\\nOdoX4ZqdAgMBAAECggEADqzUSCFxH9xZP6Cx6Z3rbLQZUN52THwxNF+da976hyaJ\\nmSHaPOCCVsyERKy9+eicvONLEof4npWYeL30LxBoCUtkHRKw48gzRy/2d731LPah\\nuVRGjasfsqFcnJOK82gE0rJ8AopFCgipleLqCPlC+Xe+K7ki3GN1dKC2XIjSV/FO\\nz/D08Yg16MEoIMCZGiPotLmQcaVE+g7BsXg/v46QyyCgyDukjkWWJumilambVIRG\\nOuVo5tAf3TPI1hk2VEZk53gI3APEnH8KuN3rsXTgZQY9C82DqZjZUgctXxu0gnGR\\nImP1GLyFmUxVte4DiT1l5Mrc5pzDYZiNyRLhZ2kEkQKBgQDaiCbdZmPxfvlckf3E\\nDwxAFPlSODUO0bp6+bwdcp9ADFk4KFJvKhQU4j2QNiARfrrgTFAgcPjOkeYxfUvu\\n8Hn2HX55egBIFG5O4RviKnIHPIajWnteXZROmKqU+NK0uSRNqIjuqvxex21CKef8\\nNnYAPaEbgGHN5A50tTvqRcOMMQKBgQDQjdV7K/tHN85LpZ7aJj+qfsbE8196hBZD\\nohNeHbiiv4yDHgknC7O8Yn+mVdW23KigWB7oqrDFhJqarfdAEx0vzUENAWRPGm0I\\n56mgss1pqllMmlOrFYLhCH2CS6jsX8n1zQH7KXOfb9NYQVDh0DuMmQIO+8j2sHog\\nD/G2OyHWLQKBgDairZzS2Y/qH+v98AURgg2PcNoWhWVkGAxg3aA7JQd9Tt0Ub6+t\\nRIIIIj4o2hGlrpEfYzUJKZtzrKqY2eAuLT/UFefHEcTznrSH4VHFLOcUQdEbcRah\\nrM+NqbA/GWbnluT3iuyowRntICrXkVFkSFI9Fkdq7IjuSJLzMLycnowxAoGBALmh\\n5alzJoDnvWo8Cz8l2HmLyqU38357381nkFGvps7GLO3waDknA17lVbXapRXVJwtC\\nJJD4jcviEjMoMfIIkWwhCIvo9z4pyW+ptKTjQk+RX1b97wdTaGGhSwYVDlEHmh59\\n0gubg90gjj/6M2IsFTU6ZEit+N0LjEjJqF6KF74pAoGADrAvgFG9k4XvgOusCzoa\\nB7x+Ih2B70w2jhQHRXN2EzExHmSdf4xKK/31jBnwK/NkG/r7CBnALo63WkQYSrmZ\\nsL1x3NA2oiPYUXrSY4k6Y0631yak93jB/RNLFjT4TQWv8Sl9/fYZvnnNDXTEaQfP\\ncXvbY4iB8Cfnp5U4d3YJzKw=\\n-----END PRIVATE KEY-----\\n",\n')
jsonWriter.write('  '+'"client_email": "firebase-adminsdk-mdv94@auction-bidding-arjun-gupta.iam.gserviceaccount.com",\n')
jsonWriter.write('  '+'"client_id": "103080961495834562053",\n')
jsonWriter.write('  '+'"auth_uri": "https://accounts.google.com/o/oauth2/auth",\n')
jsonWriter.write('  '+'"token_uri": "https://oauth2.googleapis.com/token",\n')
jsonWriter.write('  '+'"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n')
jsonWriter.write('  '+'"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-mdv94%40auction-bidding-arjun-gupta.iam.gserviceaccount.com"\n')
jsonWriter.write('}')
jsonWriter.close()
# time.sleep(5)
pATH = r'{}'.format(os.getcwd())
fILE = r"/serviceAccountKey.json"
FilePath = r'{}'.format(pATH + fILE)
#Timer
now = datetime.now()
#Initialize & Authenticate a Database
try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate(FilePath)
    firebase_admin.initialize_app(cred)
#Connect to Firestore
db = firestore.client()# this connects to our Firestore database
#for Admin &or Brokers
print("\n")
Auction_Items = db.collection(u'Auction_Items').stream()  # opens 'Auction_Items' collection
for docz in Auction_Items:
    print(f'{docz.id} => {docz.to_dict()}')
print("\n")
Choice = int(input("Which Number from the List of Items above Would You Like to Choose:"))
doc_ref = db.collection(u'Auction_Items').document(str(Choice))
docs = doc_ref.get()
if docs.exists:
    dictionarys = docs.to_dict()
    nAME = dictionarys.get('Name')
    cOST = dictionarys.get('Cost')
else:
    print(u'No such document!')
# itemNAME = input("Enter the Item Name : ")+""
print("The Auction Item is '",nAME,"' .")
print("The Starting Bid is '",cOST,"' .")
itemNAME = nAME
startingBID = cOST
#for the Dealers
count = int(input("Enter How Many Users are Participating in the Bid = "))
os.system("cls")
#StartTimer
start_time = now.strftime("%H:%M:%S")
#for Bidders
db.collection(u'Bid').document(itemNAME).delete()
Item = db.collection(u'Bid').document(itemNAME)  # opens 'Bid' collection
Type = Item.get() #type(collectionStudents.get())
#Create Users
amount = []
counter = 1
while counter <= count:
    Num = 'User'+ str(counter)
    Users = Item.collection(u'Users').document(Num)
    username = input("Enter Your Username = ")+""
    bid = int(input("Enter You Bid = "))
    os.system("cls")
    Users.set({
        'id':username,
        'amount':str(bid)
        })
    amount.append(bid)
    counter += 1
#EndTimer
end_time = now.strftime("%H:%M:%S")
#Query
maximum = max(amount)
docs = Item.collection(u'Users').where(u'amount', u"==", str(maximum)).stream()
for doc in docs:
    personNumber = doc.id
    dictionarys = doc.to_dict()
    identity = doc.get('id')
    # print(f'{doc.id} => {doc.to_dict()}')
#Create Data
Item.set({
    'starTime':str(start_time),
    'endTime':str(end_time),
    'StartPrice': startingBID,
    'WINNER': identity
    })