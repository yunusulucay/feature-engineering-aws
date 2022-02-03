# feature-engineering-aws

# Work Flow

![eda-schema](https://user-images.githubusercontent.com/42489236/152315672-89ebbdf4-9703-4cc3-9789-b846983bd0d2.jpg)

# Steps

1- Some feature engineering processes implemented on SageMaker notebook.(In notebook)

2- To make feature engineering processes created a SageMaker Processing Job.(In notebook)

3- An end-to-end feature engineering lifecycle will create. 
  a- The data send to s3 bucket.
  b- On s3 a trigger created.(When an event happens send a trigger to lambda)
  c- Lambda function created.(To get action. **-Not completed**)
  d- A docker image will create and send to ECR.(**-Not completed**)
  e- With this image on ECR i will create a SageMaker endpoint to direct lambda to.(**-Not completed**)
  f- After this endpoint triggered, input data will go through some process and train,test and val datasets will created.(**-Not completed**)
