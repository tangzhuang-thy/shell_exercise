#!/bin/bash
# **********************************************************
# * Author        : tangzhuang
# * Email         : zhuang.tang@shopee.com
# * Create time   : 2021-08-20 13:05
# * Filename      : md5_check.sh
# * Description   : check the file's md5 changed information and alert.
# **********************************************************
md5sum -c --status "$1.md5"
if [ $? == 1 ];then
	result=`md5sum -c "$1.md5"`
	echo $result | awk 'NR==1{print $1 "has been changed!"}'
	# curl -X POST -H "Content-Type: application/json" -d '<json_payload>' http://10.128.152.245:8000/v1/sre/tasks

else
	echo "$1 is normal"
fi
