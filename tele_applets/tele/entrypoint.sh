#!/bin/bash

#set -e

echo "Entering The entrypoint.sh"
echo "Setting up Pip3 dependency if any"

if [ -f /mnt/common-applets/requirements.txt ];
then
        pip3 install -r /mnt/common-applets/requirements.txt
fi

echo "Call sent for starting Tele"

/bin/bash run_tele.sh; echo "Tele Exited";


echo "Start the Exta bash"
exec /bin/bash
