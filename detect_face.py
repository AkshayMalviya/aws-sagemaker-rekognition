import boto3
import glob
import os

key ='XXXXXXXXXXXXXXXXXX'
secret = 'XXXXXXXXXXXXXXXXXXXXXXXX'
region =  'us-east-1'

#Credentials
client = boto3.client('rekognition', aws_access_key_id=key, aws_secret_access_key=secret, region_name=region )

#Created Collection Id
#response = client.create_collections(CollectionId='detect_faces')
response = client.list_collections()
collections = response['CollectionIds']
print(collections)

# Folders of different persons images
folders = ["albert","stephen"]

Uploaded Images
for folder in folders:
    for file in glob.glob(folder + "/*.jpg"):
        response = client.index_faces(
            CollectionId="detect_faces",
            Image={'Bytes': open(file, "rb").read()},
            ExternalImageId=os.path.basename(folder)
        )
        print(response)

response = client.search_faces_by_image(
    CollectionId = 'detect_faces',
    Image = {'Bytes': open("test_images/s1.jpg", "rb").read()},
  )
print(response)
print('The photo uploaded is of :'+response['FaceMatches'][0]['Face']['ExternalImageId'])