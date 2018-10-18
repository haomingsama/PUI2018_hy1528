# Homework 6 - Haoming Yang (hy1528)
----------------------------------------------------------------------------------------------------------------------------
## Assignment1:Review Comment
### I make my comment for yunhecui(yc3420) HW4 Citibike assignment
#### 1. The Null and Alternative hypothesis are formulated correctly in both words and formular. It would be better to put ‘avgtime'in the subscript like this
H<sub>0</sub> : W<sub>avgtime</sub> <= M<sub>avgtime</sub>
#### and denote that 'W' stands for women, 'M' stands for men. and 'avgtime' stands for average time of riding during the weekdays

#### 2. The data supports the project: it has the appropriate variables to answer the question, and was properly pre-processed to extract the needed columns.
#### A possible processing of the data would be extract men and women data from the gender columns, which will prepare for the further statistical testing.



#### 3. As for the test for this quesiton, since the question is do difference exist between mean women tripduration and mean men tripduration and it has two samples data(men's tripduraton data and women's tripudration data) and we don't know the population variance. Therefore, t-test can be applied here because it could use the sample variance to caculate.


#### 4.The figure gives us a very interesting observation. A validation using other months or years data to test the same question can be considered. Is there a seasonal pattern? or is this parttern only hold for some months or the hold year.

## Assignment 2 
I cooperate with xxx and xxx in this part. Please see our work below.

----------------------------------------------------------------------------------------------------------------------------
| Statistical Analyses	| IV(s)                     | IV type(s)| DV(s)                    | DV type(s)| Control Var &                                      |     Control Var type                | Question to be answered | H0                                                                                                                         | alpha| Link                                                                                                               |
|-----------------------|---------------------------|-----------|--------------------------|-----------|--------------------------------------------------------------------------|--------------------|------------------------ |---------------------------------------------------------------------------------------------------------------------------|------	|-------------------------------------------------------------------------------------------------------------------|
| Logistic Regression        	| 3 Baseline HbA1c (%). Age (years), Fractional disease duration                                                   	|Categorical  | 1, The outcome of glycaemic control, satisfatory or unsatisfatory)                                                                                                                                                                                                                                                                                                                                                                            	| Categorical                                                                                                                                                                                                           	|3.Baseline HbA1c (%) .Age (years), Fractional disease duration |  continuous                                                                                                    	|   What factors could significantly influcence the achievement of satisfactory glycaemic                                    	| Baseline HbA1c (%) /.Age (years), /Fractional disease duration could lower than or have no effect on the probability of achieving satisfactory glycaemic | 0.05	|  [Prediction of glycaemic control in young children and adolescents with type 1 diabetes mellitus using mixed-effects logistic regression modelling]( https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0182181&type=printable) 	|  	

----------------------------------------------------------------------------------------------------------------------------


## Assignment 3 
I worked alone for this part. I performed the tasks as required by the skeleton notebook and defined evalChisq function as this was mentioned in the slack chat as something that we have to define by ourselves.

## Assignment 4 
I worked alone for this part.  I started with using the helper functions that i made during HW4 that downloads multiple citibike datasets and compiles them into one dataframe. Since the assignment required atleast two months, i made use of the August and September 2018 citibike data. I've done some data exploration and outlier detection, although manually deteremined the threshold, and performed the required two sample testing.

For the extra credit problem, i took advantage of python packages Geopandas and Shapely to assist me in identifying if the Longitude and Latitude data falls under a certain borough. I took advantage of NYC Open data to get borough boundaries (https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm), since i'm encountering difficulties automating the download process of the geojson file, i've downloaded it manually and uploaded the file in my repository [here](https://raw.githubusercontent.com/jinalklaulitz/PUI2018_msm796/master/HW5_msm796/Borough%20Boundaries.geojson ). Then i checked if Long-Lat points are within the boundary <b>(NOTE: THIS TAKES REALLY LONG)</b>. From there, i did some necessarily outlier detection, exploratory data analysis and performed the required testing.

Required libraries that may not be in the default environment of the ADRF's for python 3.7:
dateutil
requests
zipfile
io
Geopandas
 Shapely
----------------------------------------------------------------------------------------------------------------------------
