#!/bin/bash

IMAGE_NAME="eu.gcr.io/uc-tri-optique-dev/wine-bot:v0.0.7"
REGION="europe-west1"
PORT=8080
MEMORY_LIMIT=2Gi
CPU=1
MAX_INSTANCES=5
CLOUD_RUN_NAME="wine-bot"


source .env

gcloud builds submit \
-t $IMAGE_NAME \
. 

#gcloud run deploy $CLOUD_RUN_NAME --image=$IMAGE_NAME \
#--platform=managed --allow-unauthenticated --region=$REGION  --port=$PORT \
#--memory=$MEMORY_LIMIT --cpu=$CPU --timeout=300 --max-instances $MAX_INSTANCES --min-instances 0
#
#gcloud beta run services update $CLOUD_RUN_NAME --session-affinity --region=$REGION
