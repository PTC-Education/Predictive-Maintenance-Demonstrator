# Python scripts for use with the Generic Analytics Thing

This directory contains the scripts and the corresponding Thingworx Thing to use Thingworx Analytics with python. The data exchange is done via the Thingworx REST API. There is one script each to train a model, query the status of the model and to perform predictions. Please have a look at the [Google Colaboratory implementation of those scripts](../Thingworx_Analytics_API_Colab_integration.ipynb) for additional information and improved usability with external data.

## Usage

In order for the scripts to work you need to import [Things_JA_Generic_Analytics_Thing.xml](Things_JA_Generic_Analytics_Thing.xml) in your Thingworx Composer. If you do not know how to import please take a look at **step 14** in the [CreateAnalyticsModel.pdf](../guides/ThingworxAnalyticsIntroduction/CreateAnalyticsModel.pdf) guide.

Please change the value of the app key in the [config.json](config.json) file to a valid application key for your Thingworx instance. 

1. Start with the [trainAnalyticsModel.py](trainAnalyticsModel.py) script. In line 15 change the url variable to the URL of your Thingworx instance. The training data must be passed as a python dictionary. Lines 144 to 149 show how the dictionary must be structured. If you want to use more features just add more key-value pairs and update the "fieldDefinitions" and "goal" of the payload variable starting at line 22. Each row needs to have the same amount of features and there can not be empty values! 

2. Execute the [trainAnalyticsModel.py](trainAnalyticsModel.py) script and copy and save the model URI.

3. Edit the [getAnalyticsModelStatus.py](getAnalyticsModelStatus.py) script: in line 15 change the url variable and in line 16 paste the model URI from the step before. Execute the script. Once the returned status is "COMPLETED" you can proceed to the next step.

4. Edit the [predictAnalyticsModel.py](predictAnalyticsModel.py) script: in line 15 change the url variable and in line 16 paste the model URI from step 2. Lines 47 to 50 show the structure of the dictionary which contains the data that is used for the real time prediction. If you want to use more data samples (e.g. time series analytics) please refer to step 1. Execute the script.

   

## Requirements:

- Completed [CreateAnalyticsModel.pdf](../guides/ThingworxAnalyticsIntroduction/CreateAnalyticsModel.pdf) guide or basic knowledge of Thingworx Analytics
- Access to Thingworx Composer
- Valid Thingworx Application Key
- Thingworx Analytics
- Python 3.7 or higher and following packages (if you use pip: `pip install package_name`)

  - requests
  - json
