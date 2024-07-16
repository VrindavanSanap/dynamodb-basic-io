import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb', "eu-north-1")

mnist_data_table = dynamodb.Table('mnist-data')
print(mnist_data_table.creation_date_time)

def add_data(data_type, index, data, label):
    mnist_data_table.put_item(
        Item={
            'data-type': data_type,
            'id': index , 
            'data': data,
            'label': label,
        }
    )


