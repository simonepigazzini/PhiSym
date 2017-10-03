#!/bin/bash

cd $CMSSW_BASE/src
mkdir -p ExternalTools

for package in CfgManager DynamicTTree FuriousPlotter
do
    set -x
    git clone -b CMSSW git@github.com:simonepigazzini/${package}.git ExternalTools/${package}
    set +x
done

scram b -j 4
