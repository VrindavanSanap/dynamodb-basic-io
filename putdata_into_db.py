import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

mnist_data_table = dynamodb.Table('mnist-data')

def add_data(data_type, index, data):
    mnist_data_table.put_item(
        Item={
            'data-type': data_type,
            'index': index,
            'data': data,
        }
    )


add_data("test", 1, "hello")
