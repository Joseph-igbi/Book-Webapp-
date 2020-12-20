#!/bin/bash
# define array
PARAMETERS=("DATABASE_URI" "MYSQL_DATABASE" "MYSQL_ROOT_PASSWORD" "SECRET_KEY")


# Constants
aws_region=eu-west-2

for par in $PARAMETERS
do
        export $par=$(aws ssm get-parameters --name $par --region=${aws_region} --output text --query "Parameters[0]"."Value");
done
