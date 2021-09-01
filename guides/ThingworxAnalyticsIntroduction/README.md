# Introduction exercise to Thingworx Analytics

This guide serves as an introductory exercise for Thingworx Analytics. This example is intended to familiarize new users with the interface and to teach them how to train a machine learning model and run predictions. 
The dataset used in this guide was generated using the following demonstrator:

<img src="/./misc/demonstrator_overview.jpg" alt="3-axis robot arm" style="zoom: 50%;" />

For more detailed information on the hardware, please navigate to the physical_demonstrator folder in this git. 
The Servo3 of the demonstrator is supposed to change its position when an additional force is applied to Servo1. In the following video you can see the live demonstration:
<img src="/./misc/machine_learning_demo.gif" style="zoom:100%;" />



## Requirements:

- Access to Thingworx Composer
- Valid Thingworx Application Key

In addition, if you want to use the hardware you need:

- Python 3.7 or higher and following packages (if you use pip: `pip install package_name`)
  - requests
  - serial
  - json
  - time

