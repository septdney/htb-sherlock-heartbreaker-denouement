import os
import gzip
import json
import uuid
import sys
from elasticsearch import Elasticsearch


def remove_trailing_slash(s):
    if s.endswith('/'):
        return s[:-1]
    return s

path_to_folder=""
if len(sys.argv) > 1:
    path_to_folder = sys.argv[1]
    path_to_folder = remove_trailing_slash(path_to_folder)
    print("Working directory is : " + path_to_folder + ".")
else:
    print("Please provide path as argument, for example : python3 Heartbreaker-Denouement.py /tmp/MySherlockFolder") 
    sys.exit(1)


print("\nCreating logs directory.")
if not os.path.exists("./logs"):
    os.makedirs(path_to_folder+"/logs")
print("OK.")


print("\nMoving Cloudtrail logs to the logs directory.")
command = "find " + path_to_folder +  "/HeartBreakerDenouement -type f -name '*.json.gz' -exec mv -i {} \\"+ path_to_folder +  r"/logs/  \;"
os.system(command)
entries = os.listdir(path_to_folder+"/logs")
file_count = sum(1 for entry in entries if os.path.isfile(os.path.join(path_to_folder+"/logs", entry)))
if file_count == 0 :
    print("Error moving logs arround... are you in the right directory ?") 
    sys.exit(1)
print("OK.")


print("\nConnecting to Elasticsearch.")
client=""
try:
    client = Elasticsearch(
    "http://localhost:9200/"
    )
    client.info()
except:
    print("Error connecting to the Elasticsearch.")
    sys.exit(1)
print("OK.")

print("\nCreating index heartbreakerdenouement.")
index_name="heartbreakerdenouement"
try:
    client.indices.create(index=index_name)
except:
    print("Index already exists.")
print("OK.")

i = 0
print("\nParsing logs and sending them to Elasticsearch, it will take a few minutes, please be patient.")
for filename in os.listdir(path_to_folder+"/logs"):
    file_path = os.path.join(path_to_folder+"/logs", filename)
    if os.path.isfile(file_path):
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            json_content = file.read()
            data = json.loads(json_content)
            if 'Records' in data :
                for record in data["Records"] :
                    if 'requestParameters' in record and  record['requestParameters'] is not None:
                        if "DescribeSecurityGroupRulesRequest" in record['requestParameters']:
                            del record['requestParameters']["DescribeSecurityGroupRulesRequest"]
                    if 'requestParameters' in record and  record['requestParameters'] is not None:
                        if "DescribeLaunchTemplatesRequest" in record['requestParameters']:
                            del record['requestParameters']["DescribeLaunchTemplatesRequest"]
                    if 'requestParameters' in record and  record['requestParameters'] is not None:
                        if "DescribeTransitGatewaysRequest" in record['requestParameters']:
                            del record['requestParameters']["DescribeTransitGatewaysRequest"]
                    if 'requestParameters' in record and  record['requestParameters'] is not None:
                        if "DescribeVpcEndpointsRequest" in record['requestParameters']:
                            del record['requestParameters']["DescribeVpcEndpointsRequest"]
                    log_id = str(uuid.uuid4())
                    try :
                        response = client.index(index=index_name, id=log_id, body=record)
                    except Exception as e: 
                        print("\nSome parsing exception that we can ignore... " + str(e))
    i = i + 1
    if i % 500 == 0 :
        print("\nStill working...")
print("\n\nDone, you can now visit http://127.0.0.1:5601/")
