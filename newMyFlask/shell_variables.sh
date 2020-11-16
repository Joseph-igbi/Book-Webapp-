#!/bin/bash

aws_region=eu-west-2

for i in DATABASE_URI2 MYSQL_DATABASE MYSQL_ROOT_PASSWORD SECRET_KEY

do
	#echo $(aws ssm get-parameters --name=$i --region=${aws_region} --output text --query "Parameters[0]"."Value");
	echo export $i=$(aws ssm get-parameters --name=$i --region=${aws_region} --output text --query "Parameters[0]"."Value");


done	
