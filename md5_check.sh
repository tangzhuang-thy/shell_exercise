#!/bin/bash
# **********************************************************
# * Author        : tangzhuang
# * Email         : zhuang.tang@shopee.com
# * Create time   : 2021-08-20 13:05
# * Filename      : md5_check.sh
# * Description   : check the file's md5 changed information and alert.
# **********************************************************
# create file's new md5 value
md5_new=$(md5sum $1 | awk '{print $1}')

function createmd5(){
	echo $md5_new > $1.md5
}
# check file's md5 existed status
if [ ! -f "$1.md5" ]
then echo "md5file is not existed,create one."
	createmd5 "$@"
fi

md5_old=$(cat "$1.md5")

if [ "$md5_new" == "$md5_old" ];then echo "$1 is normal."
else echo "$1 has been changed!"
# curl -X POST -H "Content-Type: application/json" -d '<json_payload>' http://10.128.152.245:8000/v1/sre/tasks
fi
