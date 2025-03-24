# TOR-NODES-REQUEST
TOR End-Nodes request for waf - Aws - Firewall

# m10secœproton.me

## TOR Exit Node Blocker for AWS WAF
This Python script automatically fetches the list of TOR exit nodes and updates an AWS WAF IP set with the current TOR IPs. This helps block or monitor traffic from the TOR network in your CloudFront distribution.

⚙️ Features
✅ Fetches the latest TOR exit node list from torproject.org
✅ Updates an AWS WAF IP set with the TOR exit IPs
✅ Supports CloudFront distributions

🛠️ Requirements
Python 3.x

boto3 for AWS interaction

requests for fetching the TOR exit node list

Install Dependencies:
bash
Copy
Edit
pip install boto3 requests
🔥 Usage
Set up AWS credentials
Ensure you have valid AWS credentials configured (either using aws configure or environment variables).

Run the script
Replace the placeholders with your AWS WAF IP set ID and name:

bash
Copy
Edit
python tor_waf_updater.py
Parameters

ip_set_id: The ID of the AWS WAF IP set you want to update.

ip_set_name: The name of the AWS WAF IP set.

region: (Optional) AWS region, defaults to us-east-1.

🌐 Example
python
Copy
Edit
ip_set_id = 'your-ip-set-id'
ip_set_name = 'your-ip-set-name'
region = 'us-east-1'

update_ip_set(ip_set_id, ip_set_name, region)
⚠️ IAM Permissions Required
Ensure your AWS IAM role or user has the following permissions to update the WAF IP set:

json
Copy
Edit
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "wafv2:UpdateIPSet",
                "wafv2:GetIPSet"
            ],
            "Resource": "*"
        }
    ]
}
🚀 Deployment
You can schedule this script with a cron job or AWS Lambda function to keep your WAF IP set up to date regularly.
Example cron job to run every hour:

ruby
Copy
Edit
0 * * * * /usr/bin/python3 /path/to/tor_waf_updater.py
🛠️ Troubleshooting
botocore.exceptions.NoCredentialsError: Ensure your AWS credentials are properly configured.

AccessDeniedException: Verify your IAM role has the necessary permissions.

Rate limits: AWS WAF may have rate-limiting policies; avoid frequent updates.

📝 License
MIT License. Feel free to use, modify, and distribute this script.
