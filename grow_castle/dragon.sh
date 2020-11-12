#!/bin/bash
for i in {1..1000}
do
   echo "Welcome $i times"
   adb shell input tap 900 300
   adb shell input tap 1800 500
   adb shell input tap 1800 500
   sleep 35
   adb shell input tap 1000 800
done
