# Predictive-Maintenance-Demonstrator
This repository contains tutorials for using Thingworx Analytics for a predictive maintenance use case. The aim of this project is to develop a low cost demonstrator that can be used to show basic concepts of predictive maintenance. In the course of this project, guides were created on how to create time series and non time series models with the help of Thingworx Analytics. These guides should make it easier for users to get started with Thingworx Analytics and predictive maintenance.

## Overview:
This project is intended to serve as a foundation for students and new users of Thingworx Analytics to gain a basic understanding of the Analytics platform as well as the implementation of predictive maintenance projects. The hardware used is an inexpensive robot arm that can be easily replicated. The use of real hardware is intended to provide a reference to the data used, as opposed to the often arbitrary data sets provided for training. 
In addition, a Google Colab document is provided to make Thingworx Analytics available as a service. Users do not need to have access to a Thingworx portal and can still use the basic functionalities. The data sets are read in via Google spreadsheets, which ensures an easier overview of the data for the user and reduces the time required to make changes to the data set.

# Structure:
1. **guides**
   In this directory you will find the created guides for the use of Thingworx Analytics and a [guideline](/guides/ThingworxAnalyticsTimeSeriesPrediction/GuidelineThingworxAnalytics.pdf) for the planning of a predictive maintenance project. The guides can be used without access to the hardware as well.
2. **physical_demonstrator**
   This directory contains the software for the communication of the robot arm with a Raspberry Pi or PC via USB
3. **thingworx_analytics_scripts**
   This folder contains scripts and associated Thingworx Things to use Analytics functions via the Thingworx REST interface.
4. **Thingworx_Analytics_API_Colab_integration**
   This Google Colaboratory notebook allows users to use data sets from Google Spreadsheets with Thingworx Analytics without needing access to Thingworx Composer. (Thingworx Analytics as a service)





