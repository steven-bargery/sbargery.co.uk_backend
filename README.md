# sbargery.co.uk - backend

This repository contains two AWS Lambda functions, written in Python, that GET and POST data from a DynamoDB table for my website [sbargery.co.uk](https://www.sbargery.co.uk).

These functions were created to display an up-to-date count of the number of visitors to my website.

Once pushed to Github, using Github Actions, both functions are tested using pytest with their corresponding test_*.py files and are then deployed to AWS Lambda.

## create_visitor.py

[![Actions Status](https://github.com/steven-bargery/sbargery.co.uk_backend/workflows/deploy%20create_visitor%20to%20lambda/badge.svg)](https://github.com/steven-bargery/sbargery.co.uk_backend/actions)

This function creates an entry in the DynamoDB table that contains the current date and time and the IP address of the visitor.

## get_visitors.py

[![Actions Status](https://github.com/steven-bargery/sbargery.co.uk_backend/workflows/deploy%20get_visitors%20to%20lambda/badge.svg)](https://github.com/steven-bargery/sbargery.co.uk_backend/actions)

This function returns the number of entries in the DynamoDB table.