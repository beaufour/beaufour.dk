#!/usr/bin/env bash
DEST=$1
if [ -z "$DEST" ]; then
    DEST=test
fi
BUCKET=$DEST.beaufour.dk
echo Upload to: $BUCKET
read -p "Are you sure? " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi
aws s3 sync --acl public-read --exclude "*.git*" --exclude "*.DS_Store" --exclude "upload.sh" . s3://$BUCKET/
