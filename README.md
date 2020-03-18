# How To Run
Note: I am using Python 2.7

Note: I know I am using camel case and python should be snake case. Force of habit.

## Generating Random Sequences
`python ./TrainingSetGeneration.py`  
This will create 100 files (from 0-99) of 10 random sequences terminating in either G or A. The sequences will be of the form `DEFG` or `DCDCBA` as examples.
Every time it runs it will generate new files (I don't have a seed value) so be careful to not overwrite the files for all experiments.  
The trainingSetxx.txt given in this repo are the training sets I use for the probability estimator.

## Running the Probability Estimator
`python ./ProbabilityEstimator.py <alpha> <lambda>`
This assumes you have already run the TrainingSetGeneration.py file above as it will read from these files.  
This will run the experiment as given for Figure 4 with the correct equation 4 in Sutton's paper. That is, it will update after every sequence NOT after every training set.  
If you want to run with the method given in Figure 3, uncomment line 25 and comment line 24 in `ProbabilityEstimator.py`. This will run the no updating per sequence method.  
The output of this file will be `alpha: <alphaVal> lambda: <lambdaVal> RMSE: <rmse>` and will output in `rmse3.txt`. The RMSE for the program is the root mean squared error of the 100 training sets.  
Note: each time you run the program it will append to `rmse3.txt`. It will NOT overwrite it.

## Creating the Graphs
`python ./graphCreator.py`  
This will create three graphs: `graph3.png`, `graph4.png`, and `graph5.png` which correspond to the figures in Sutton's paper respectively.  
If you want to create new graphs with your values from the experiment, you will have to go into the python file and manually update the data values (x values).  

## Other notes
`lambdaAlphaValues.txt` has the RMSE for lambdas from 0.0 to 1.0 in 0.1 increments for alphas 0.0 to 0.5 (or something like that) in increments of 0.05.  
This information is what I used for figure 5.  
If you're running a lot of experiments at once, I recommend using `bash.sh` with your commands that you want to use.
