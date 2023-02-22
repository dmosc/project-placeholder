#!bin/bash

CHECKSUM="\"$((RANDOM))\""

curl -s -X POST -H "Content-Type: application/json" -d '{"name": '$CHECKSUM', "email": '$CHECKSUM', "content": '$CHECKSUM'}' http://142.93.11.21:5000/api/create_post
EMAIL_OF_LAST_POST=$(curl -X GET http://142.93.11.21:5000/api/get_posts | jq '.posts[0].email')

if [[ $CHECKSUM == $EMAIL_OF_LAST_POST ]]; then
  echo "Post creation works."
else
  echo "There's an issue with post creation."
fi
