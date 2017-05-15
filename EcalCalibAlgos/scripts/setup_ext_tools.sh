#!/bin/bash

cd $CMSSW_BASE/src
mkdir -p ExternalTools/

packages="CfgManager DynamicTTree FuriousPlotter"

for package in $packages
do
    git clone -b CMSSW git@github.com:simonepigazzini/$package.git ExternalTools/$package 
done

scram b -j 4
