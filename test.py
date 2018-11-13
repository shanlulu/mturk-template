import boto3

region_name = 'us-east-1'
aws_access_key_id = 'AKIAI3HZGBXJZYLFAN7Q'
aws_secret_access_key = '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'

endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# This will return $10,000.00 in the MTurk Developer Sandbox
print(client.get_account_balance()['AvailableBalance'])
