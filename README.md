# To deploy in docker you need to register:
  docker build https://github.com/Famerttt/validator.git -t validator -f ./Docker/Dockerfile
# container launch
 docker run validator
# input data
{'file', 'targetName', 'errorCode'}

# output data 
{
    "anomaly": true,
    "error_message": "",
    "fault": true,
    "rul": true,
    "validationStatus": true
}
