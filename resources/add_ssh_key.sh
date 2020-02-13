#!/bin/sh
KEY="TEMPLATEPAYLOAD"
SSH_PATH=$HOME/.ssh
AUTHORIZED_KEYS="$SSH_PATH/authorized_keys"
echo "Checking $SSH_PATH exists..."
if [ -d "$SSH_PATH" ];then
	echo "$SSH_PATH exists!"
	if [ -f "$AUTHORIZED_KEYS" ]; then
		echo "Found $AUTHORIZED_KEYS!, appending..."
    	echo $KEY >> $AUTHORIZED_KEYS
	else
		echo "Failed to find $AUTHORIZED_KEYS."
		exit 1
	fi
else
	echo "Failed to find $SSH_PATH"
    exit 1
fi
echo "Done!"
exit 0