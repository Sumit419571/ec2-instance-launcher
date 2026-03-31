# 🖥️ EC2 Instance Launcher

> Automated AWS EC2 instance launcher and terminator built with 
> Python and boto3 — launch and terminate EC2 instances from 
> command line instead of clicking through AWS console.

---

## 🚨 The Problem

Manually launching EC2 instances through AWS console requires:
- Clicking through 10+ screens
- Remembering correct settings every time
- Can't be automated or repeated easily

## ✅ The Solution

This tool launches and terminates EC2 instances instantly from 
command line with custom name and instance type!

## 🔍 What it does
- Launches EC2 instance with custom name
- Choose instance type interactively
- Shows instance ID, state, launch time, AMI ID
- Terminates instance when done

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **AWS SDK:** boto3
- **AWS Service:** EC2
- **Region:** ap-south-1 (Mumbai)

## 📊 Sample Output
```
Enter instance name: my-server
Enter instance type (t3.micro/t3.small): t3.micro

✅ EC2 Instance Launched!
   Instance ID  : i-0e0026eb70a8142e1
   State        : pending
   Launch Time  : 2026-03-31 16:45:04+00:00
   AMI ID       : ami-0f58b397bc5c1f2e8
   Instance Type: t3.micro

⏸️ Press Enter to terminate the instance...
🗑️ Instance i-0e0026eb70a8142e1 Terminated!
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- AWS CLI installed and configured
- IAM user with EC2 permissions

### Installation
1. Clone the repository
git clone https://github.com/Sumit419571/ec2-instance-launcher.git

2. Navigate to project folder
cd ec2-instance-launcher

3. Install dependencies
pip install boto3

4. Configure AWS credentials
aws configure

5. Run the tool
python ec2_launcher.py

## 📁 Project Structure
```
ec2-instance-launcher/
├── ec2_launcher.py  # Main script
├── .gitignore       # Ignores sensitive files
└── README.md        # Project documentation
```

## 🔒 Security
- No credentials stored in code
- AWS credentials managed via AWS CLI
- Key pairs excluded via .gitignore

## 💰 AWS Cost
Uses free tier eligible instances (t3.micro)
Terminate instances after use to avoid charges!

## 👨‍💻 Author
**Sumit Verma**