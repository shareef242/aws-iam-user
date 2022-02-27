import boto3
import random
import string

iam = boto3.resource('iam')
iam_keys = boto3.resource('iam')
group_list = boto3.client('iam')
attach_group = boto3.client('iam')
grp = boto3.client('iam')
client = boto3.client('iam')

user = $1
response = iam.create_user(UserName="${user}")
print(response)

#get random pass
characters = string.acsii_letters + string.digits + string.punctuation
password = ''.join(random.coice(characters) for i in range(12))
print("random password is:", password)

response1 = client.create_login_profile(
    UserName=user,
    Password=password,
    PasswordResetRequired=True
)
print(response1)

list = group_list.list_groups()
groups = list['Groups']
print(groups)
index = 1

for group in groups:
    print("%d: %s" % (index, group["GroupName"]))
    index +=1
    
group_option = int(input("Please pick a Group Number: "))
arn = groups[group_option-1]["Arn"]
print("You selected option %d: %s" % (option, arn))

var = "%s" % (arn)
var.split(":group/")[1]

group = groups[group_option-1]
group_name = group["GroupName"]
group_arn = group["Arn"]

final = grp.add_user_to_group(GroupName=group_name, UserName=user)
print("User has been addedto Group %s you selected" % (group_name))
