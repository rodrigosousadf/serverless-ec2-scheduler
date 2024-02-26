import boto3

def lambda_handler(event, context):
    # Inicializar o cliente EC2
    ec2_client = boto3.client('ec2', region_name='ap-south-1') 

    # Especifica a instance Id da EC2 que você quer iniciar
    instance_id = 'i-02c062b8447ffe813' # Replace your Own Instance ID

    # Inicia a instância EC2
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(f"Starting EC2 instance {instance_id}...")
        print(f"Response: {response}")
        return {
            'statusCode': 200,
            'body': f"EC2 instance {instance_id} is being started."
        }
    except Exception as e:
        print(f"Error starting EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Error starting EC2 instance: {str(e)}"
        }
