# Introduction exercise to Predictive Maintenance using Thingworx Analytics

This guide serves as an introductory exercise for a predictive maintenance use case using Thingworx Analytics. This example is intended to familiarize new users with the necessary steps for a predictive maintenance project and time series Analytics with the Analytics builder. Before you start the project please read through the [guideline for a predictive maintenance project](GuidelineThingworxAnalytics.pdf) before.
The dataset used in this guide was generated using the following demonstrator:

<img src="/./misc/demonstrator_overview.jpg" style="zoom: 50%;" />

For more detailed information on the hardware, please navigate to the physical_demonstrator folder in this git. 
The robot arm is drawing a line on paper with a mechanical pencil:

<img src="/./misc/predictive_maintenance_data_collection.gif" style="zoom:100%;" />

One cycle of the program includes a left to right movement where the robot arm draws a line on a sheet of paper and then the movement back to the start position without drawing. The goal of this project is to use the available data from the servo motors and the timestamps to train a model that can be used to predict the remaining useful life (how many cycles it will take before no more line is drawn) of the pencil tip. 

## Requirements:

- Access to Thingworx Composer
- Valid Thingworx Application Key
- Thingworx Analytics

In addition, if you want to use the hardware you need:

- Python 3.7 or higher and following packages (if you use pip: `pip install package_name`)
  - requests
  - serial
  - json
  - time
  - pandas

