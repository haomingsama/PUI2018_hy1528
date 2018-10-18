**Hi, this is Jianwei Li, I am trying to make comment of your Assignment2_hy1528**

# HW5 Assignment 1


a) Review Null and alternative hypothesis

Haoming's Null hypothesis is Whether the tripduration time varies between weekdays and weekend? Will people ride longer in weekends? 

I think this Null hypothesis could be like as below. I think your statement is very straight forward

H0:  The tripduration time in weekday is longer or equal than their tripduration in weekend
T(weekdays) - T(weekend) >=0
H1:  The tripduration time in weekday is smaller than their tripduration in weekend
T(weekdays) - T(weekend) < 0


b) Verify that the data supports the project 

It looks like haoming choose not only the tripduration gender and he also seperate the weekdays and weekend using dt.weekday function 



c) choose an appropriate test

from the plot figure 1.1 is a good way to show the weekend tripduration is longer weekdays.

we use the t-test for the total population, female population and  male population to reject null hypothesis

Also he use another dataset to test the same hypothesis using the 201712 dataset. 
It still can reject his null hypothesis  for the total population, but the female and male population does not reject the null hypothesis.

Finally, I agree his robustness test by using another dataset to test his null hypothesis. I believe it could be better with he can combine a dataset and do the cross validation to do t-test which can produce a more reliable result.



