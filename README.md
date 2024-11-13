# BrisT1D-Blood-Glucose-Prediction
Term Project for CS 437 - Introduction to Machine Learning\
Kaggle competition for BrisT1D Blood Glucose Prediction:
https://www.kaggle.com/competitions/brist1d/overview

# Description
## Type 1 Diabetes
Type 1 diabetes is a chronic condition in which the body no longer produces the hormone insulin and therefore cannot regulate the amount of glucose (sugar) in the bloodstream. Without careful management, this can be life-threatening and so those with the condition need to inject insulin to manage their blood glucose levels themselves. There are many different factors that impact blood glucose levels, including eating, physical activity, stress, illness, sleep, alcohol, and many more, so calculating how much insulin to give is complex. The continuous need to think about how an action may impact blood glucose levels and what to do to counteract it is a significant burden for those with type 1 diabetes.

An important part of type 1 diabetes management is working out how blood glucose levels are going to change in the future. Algorithms of varying levels of complexity have been developed that perform this prediction but the messy nature of health data and the numerous unmeasured factors mean there is a limit to how effective they can be. This competition aims to build on this work by challenging people to predict future blood glucose on a newly collected dataset.

## The Dataset
The data used in this competition is part of a newly collected dataset of real-world data collected from young adults in the UK who have type 1 diabetes. All participants used continuous glucose monitors, and insulin pumps and were given a smartwatch as part of the study to collect activity data. The complete dataset will be published after the competition for research purposes. Some more details about the study can be found in this blog post.

# Dataset Description
The dataset is from a study that collected data from young adults in the UK with type 1 diabetes, who used a continuous glucose monitor (CGM), an insulin pump and a smartwatch. These devices collected blood glucose readings, insulin dosage, carbohydrate intake, and activity data. The data collected was aggregated to five-minute intervals and formatted into samples. Each sample represents a point in time and includes the aggregated five-minute intervals from the previous six hours. The aim is to predict the blood glucose reading an hour into the future, for each of these samples.

The training set takes samples from the first three months of study data from nine of the participants and includes the future blood glucose value. These training samples appear in chronological order and overlap. The testing set takes samples from the remainder of the study period from fifteen of the participants (so unseen participants appear in the testing set). These testing samples do not overlap and are in a random order to avoid data leakage.

## Complexities to be aware of:
1. this is medical data so there are missing values and noise in the data
2. the participants did not all use the same device models (CGM, insulin pump and smartwatch) so there may be differences in the collection method of the data\
3. some participants in the test set do not appear in the training set
## Files
1. activities.txt - a list of activity names that appear in the activity-X:XX columns
2. sample_submission.csv - a sample submission file in the correct format
3. test.csv - the test set
4. train.csv - the training set

## Columns:
train.csv
1. id - row id consisting of participant number and a count for that participant
2. p_num - participant number
3. time - time of day in the format HH:MM:SS
4. bg-X:XX - blood glucose reading in mmol/L, X:XX(H:MM) time in the past (e.g. bg-2:35, would be the blood glucose reading from 2 hours and 35 minutes before the time value for that row), recorded by the continuous glucose monitor
5. insulin-X:XX - total insulin dose received in units in the last 5 minutes, X:XX(H:MM) time in the past (e.g. insulin-2:35, would be the total insulin dose received between 2 hours and 40 minutes and 2 hours and 35 minutes before the time value for that row), recorded by the insulin pump
6. carbs-X:XX - total carbohydrate value consumed in grammes in the last 5 minutes, X:XX(H:MM) time in the past (e.g. carbs-2:35, would be the total carbohydrate value consumed between 2 hours and 40 minutes and 2 hours and 35 minutes before the time value for that row), recorded by the participant
7. hr-X:XX - mean heart rate in beats per minute in the last 5 minutes, X:XX(H:MM) time in the past (e.g. hr-2:35, would be the mean heart rate between 2 hours and 40 minutes and 2 hours and 35 minutes before the time value for that row), recorded by the smartwatch
8. steps-X:XX - total steps walked in the last 5 minutes, X:XX(H:MM) time in the past (e.g. steps-2:35, would be the total steps walked between 2 hours and 40 minutes and 2 hours and 35 minutes before the time value for that row), recorded by the smartwatch
9. cals-X:XX - total calories burnt in the last 5 minutes, X:XX(H:MM) time in the past (e.g. cals-2:35, would be the total calories burned between 2 hours and 40 minutes and 2 hours and 35 minutes before the time value for that row), calculated by the smartwatch
10. activity-X:XX - self-declared activity performed in the last 5 minutes, X:XX(H:MM) time in the past (e.g. activity-2:35, would show a string name of the activity performed between 2 hours and 40 minutes and 2 hours and 35 minutes before the time value for that row), set on the smartwatch
11. bg+1:00 - blood glucose reading in mmol/L an hour in the future, **this is the value you will be predicting (not provided in test.csv)**

# Submission File
For each ID in the test set, you must predict a blood glucose value an hour into the future. The file should contain a header and have the following format:
```
id,bg+1:00
p01_0,6.3
p01_1,6.3
p01_2,6.3
etc.
```
