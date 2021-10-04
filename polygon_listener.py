import time

from polygon import WebSocketClient
import boto3
import json
import decimal
import os


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('polygon-options-trades')

def my_custom_process_message(message):
    message = json.loads(message, parse_float=decimal.Decimal)
    print(message)
    # if isinstance(message, list):
    #     for item in message:
    #         print(item)
    #         if item['ev'] == 'T':
    #             resp = table.put_item(Item=item)
    # else:
    #     if message['ev'] == 'T':
    #         resp = table.put_item(Item=message)
    #         print(message)
    # print(resp)

def my_custom_error_handler(ws, error):
    print("this is my custom error handler", error)


def my_custom_close_handler(ws):
    print("this is my custom close handler")


def main():
    key = os.environ['POLYGON_API_KEY']
    my_client = WebSocketClient('options', key, my_custom_process_message)
    my_client.run_async()

    my_client.subscribe("T.*")


if __name__ == "__main__":
    main()
