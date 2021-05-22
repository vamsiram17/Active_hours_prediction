# Active_hours_prediction
This project is predicting number of hours a person can be active in a day based on the amount of sleep the person got in the night.

## Dataset:

I have formulated a dataset containing **two columns** namely **Time slept(in hrs)** and **Time active(in hrs)**.This dataset consists of 432 records of number of hours slept during the night and correspondingly the number of hours the person was active in the following day.

With the help of the above dataset,I developed a machine learning model such that if given the number of hours slept as input,the model will predict the possible number of hours that person might be active in the day.

- input: number of hours slept during night
- output: possible number of hours the person might be active


## Choosing and Evaluating the model:

As it is clear by now that both the input and output variables are in numbers and we should choose a **Regrerssion model** accordingly.Initially I tried to fit LinearRegression model but found that most of the datapoints were not fit by the line and the model did not perform well.Then I tried fitting the data to **RandomForestRegressor** and obtained considerably good predicting performance by the model.

The process of visualizing the datapoints and the model development is attached in the python notebook which is present in this repository.

## Deploying the model to Webapp using Flask:

- **index.html**:

As soon as the webapp is launched the user will be able to see index page where there would be a form having 2 fields and 2 buttons,
Your name : Text field
Hours you slept: Text field
Submit and Reset Buttons.

- **web_app**:

You can observe in the python notebook as we have developed the **model** and **saved** it **into a pkl file** using the python pickle library.
This pkl file is used to predict the input which would be given by the user in the webapp.

- **success.html**:

On clicking the submit button the user will be directed to this page which displays the user's name, hours slept and as per the hours slept it gives the predicted value for how many hours the user be active in the day.

- **templates**:

This folder contains the files of index.html and success.html.
