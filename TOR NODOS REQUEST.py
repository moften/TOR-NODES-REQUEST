import requests
import boto3
 
def get_tor_exit_nodes():
    response = requests.get('https://check.torproject.org/torbulkexitlist')
    return response.text.splitlines()
 
def update_ip_set(ip_set_id, ip_set_name, region='us-east-1'):
    client = boto3.client('wafv2', region_name=region)
    ip_addresses = get_tor_exit_nodes()
    response = client.update_ip_set(
        Name=ip_set_name,
        Scope='CLOUDFRONT',
        Id=ip_set_id,
        Addresses=ip_addresses
    )
    return response
 
if __name__ == '__main__':
    ip_set_id = 'your-ip-set-id'
    ip_set_name = 'your-ip-set-name'
    update_ip_set(ip_set_id, ip_set_name)