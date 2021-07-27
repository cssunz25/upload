
ant_input=`cat /dev/stdin`
a#!/bin/sh

cd /tmp && curl -kLsO https://raw.githubusercontent.com/minershive/hiveos-asic/master/hive/bin/selfupgrade && sh selfupgrade 0.1-13 --force --farm-hash=e4b78447310daac3d0e0f86bc527de49eaa1c1c3
