#!/bin/env bash

# define array
PARAMETERS=DATABASE_URI2 MYSQL_DATABASE MYSQL_ROOT_PASSWORD SECRET_KEY


# Constants
aws_region=eu-west-2
# get length of an array
tLen=${#PARAMETERS[@]}
# use for loop read all parameters
for (( i=0; i<${tLen}; i++ ));
do
export ${PARAMETERS[$i]}=$(aws ssm get-parameters --name ${PARAMETERS[$i]} --region=${aws_region} --output text --query "Parameters[0]"."Value");
done
#echo ${PARAMETERS[$i]}
#done



