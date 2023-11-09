import json
import boto3
import os
import sys
import uuid
import time
from botocore.vendored import requests
import urllib3
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
ES_HOST = 'search-photos-ftjcbzutcrr3guaf6cd4upfafy.us-east-1.es.amazonaws.com'
REGION = 'us-east-1'
INDEX=""
variable="hello world"
def get_url(es_index, es_type, keyword):
    url = ES_HOST + '/' + es_index + '/' + es_type + '/_search?q=' + keyword.lower()
    return url

def get_awsauth(region, service):
    cred = boto3.Session().get_credentials()
    return AWS4Auth(cred.access_key,
                    cred.secret_key,
                    region,
                    service,
                    session_token=cred.token)
def open_search(term):
    q = {"query": {"match": {"labels": term}}}
    print("q: ",q)
    client = OpenSearch(hosts=[{
        'host': ES_HOST,
        'port': 443
    }],
        http_auth=get_awsauth(REGION, 'es'),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection)
    print("client: ",client)
    res = client.search(q)
    print("res: ",res)

    hits = res['hits']['hits']
    results = []
    for hit in hits:
        results.append(hit['_source'])

    return results

def lambda_handler(event, context):
    # recieve from API Gateway
    print("EVENT --- {}".format(json.dumps(event)))
    print("context: ", context)
    headers = {"Content-Type": "application/json"}
    lex = boto3.client('lexv2-runtime')

    query="show me cat"

    lex_response = lex.recognize_text(
            botId='QSLFXPY4IU', # MODIFY HERE
            botAliasId='MNEGZHCC1E', # MODIFY HERE
            localeId='en_US',
            sessionId='testuser',
            text=query)

    print("LEX RESPONSE --- {}".format(json.dumps(lex_response)))

    slots = lex_response["interpretations"][0]["intent"]['slots']

    img_list = []
    for i, tag in slots.items():
        print("i: ",i)
        print("tag: ",tag)
        if tag:
            tag=tag['value']['interpretedValue']
            url = get_url('photos', 'Photo', tag)
            print("ES URL --- {}".format(url))
            es_response = open_search(tag)
            print("ES RESPONSE:",es_response)

            es_src = es_response
            print("ES HITS --- {}".format(json.dumps(es_src)))

            for photo in es_src:
                print("photo data: ",photo)
                labels = [word.lower() for word in photo['labels']]
                if tag in labels:
                    objectKey = photo['objectKey']
                    img_url = 'https://s3.amazonaws.com/cc3-photos/' + objectKey
                    img_list.append(img_url)

    if img_list:
        print("images data: ",img_list)
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                'Content-Type': 'application/json'
            },
            'body': json.dumps(img_list)
        }
    else:
        print("no images or something went wrong lol")

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                'Content-Type': 'application/json'
            },
            'body': json.dumps("No such photos.")
        }
