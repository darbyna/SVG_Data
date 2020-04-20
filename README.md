# Data Analysis: Demographic and Geographic Patterns of Cetacean-based Food Product Consumption and Potential Mercury Exposure within a Caribbean Whaling Community


## Introduction

This data analysis will focus on observing the occupations and diets of the citizens of Saint Vincent and the Grenadines. Python and R code will be utilized to attain a model for whether the differences in consumption patterns by occupational category are independent of each respondent's gender or are different based on gender predisposition toward certain occupations. Another model will be concocted that focuses on whether the apparently slight differences among consumption patterns by age category are statistically significant. 

Data for this project is essential and examining the method by which the data was compiled is also of utmost importance, hence this Github page.

## Figures 

In this data analysis, you will come upon a plethora of different figures. Please find below a pre-print of each figure that is constructed in the code: 






## Package Installations 

It is necessary to install the following packages if attempting to recapitulate this project. With the packages listed below, you will be able to compile data and utilize the tools necessary for concocting a proper survey code:

pandas
numpy
matplotlib.pyplot


Upon installation of the packages above, be certain to patch the "matplotlib.pyplot" package to ensure that your charts are able to be displayed upon calling the ".show()" operation. 


## Linking Your Data

Many individuals encounter predicaments when attempting to import their data into their shell. To solve this issue, ensure that your data is in an Excel file, in a table-based format. Then, save your Excel file as a ".csv" file. In chronological order, you must first click "save as..". Proceeding this step, you must click the options for the file save. Then, you click ".csv" and finally complete the save.

After this is complete, you will use the pandas function: pd.read_csv(). As a key step, you must write pd.read_csv(r" the path to your file "). Many may wonder how the path to their file looks. It may be displayed as something like this: "C:\Users\admin\documents\csv_file_name". Of course, you will set this read equal to, for example, "Data" , and begin constructing your charts and graphs from there.


## Possible References 

When developing any coding program, it is quite pleasant to detail any help you received. Credit will go to the following website(s):

www.stackoverflow.com

The stackoverflow website was of immense assistance while developing this project. There were many bugs that required cleansing and stackoverflow assisted with tips and guidance as to how to eradicate them.



