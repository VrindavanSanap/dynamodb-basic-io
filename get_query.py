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

def get_item(data_type, id):
    table = mnist_data_table
    try:
        response = table.get_item(Key={'data-type': data_type, 'id': id})
        item = response.get('Item')

        if not item:
            print(404, f"Item with data_type {data_type} and ID {id} not found")
        else:
            return (item)

    except Exception as e:
        print(500, f"Failed to fetch item: {str(e)}")

print(get_item("train", 0))

