import boto3
import json 
# Get the service resource.
dynamodb = boto3.resource('dynamodb', "eu-north-1")

mnist_data_table = dynamodb.Table('mnist-data')

def add_data(data_type, index, data):
    mnist_data_table.put_item(
        Item={
            'data-type': data_type,
            'index': index,
            'data': data,
        }
    )

def get_item(data_type, id):
    table = mnist_data_table
    try:
        response = table.get_item(Key={'data-type': data_type, 'id': id})
        item = response.get('Item')

        if not item:
            print(404, f"Item with data_type {data_type} and ID {id} not found")
        else:
            return json.dumps(item)

    except Exception as e:
        print(500, f"Failed to fetch item: {str(e)}")


