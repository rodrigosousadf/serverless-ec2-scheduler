import boto3

def lambda_handler(event, context):
    # Inicializa o cliente EC2
    ec2_client = boto3.client('ec2', region_name='us-east-1') # Replace your Region name

    # Especifica a instance Id da instancia EC2 que você quer pausar
    instance_id = 'i-02c062b8447ffe813' # Replace your Own Instance ID

    # Pausa a instancia EC2
    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(f"Stopping EC2 instance {instance_id}...")
        print(f"Response: {response}")
        return {
            'statusCode': 200,
            'body': f"EC2 instance {instance_id} is being stopped."
        }
    except Exception as e:
        print(f"Error stopping EC2 instance: {e}")
        return {
            'statusCode': 500,
            'body': f"Error stopping EC2 instance: {str(e)}"
        }
