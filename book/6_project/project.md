# Computing Project
For the rest of this course you will put together the concepts and skills you have learnt so far in order to conduct a simple (but genuine) scientific experiment.

## Introduction

It is well known that the value of [acceleration due to gravity at the Earth's surface ($g$)](https://en.wikipedia.org/wiki/Gravity_of_Earth) is approximately $9.81~\mathrm{m}/\mathrm{s}^2$. But how accurately can you measure the value of this physical constant using just a handheld video camera and your nascent programming skills?

:::{admonition} Project Goal
:class: tip
Perform an experiment to determine an estimate of the value of $g$, using a handheld camera to capture the experimental results and Python to perform the analysis.
:::

## Instructions

These instructions are one suggested way to meet the project goal. There may be other equally valid ways to achieve the goal, so feel free to adapt them as you wish.

### Step 1: Conduct an Experiment

Using a handheld video camera (e.g. the one in your smartphone), record the motion of an object falling vertically from rest. You can use any object you like, but I advise against anything breakable or expensive. You might need to experiment a little to determine a setup which reliably gives a clean and accurate recording (for example the camera will need to be completely static) but don't spend a lot of time tinkering; you can refine the experiment later! The output of this step should be a movie file (e.g. `.mov` or `.avi`).

### Step 2: Extract the Data

Extract the location of the object from the recording in the form of a sequence of x and y co-ordinates for each frame. First you will need to upload the movie file. Then you can use the image segmentation techniques studied in the last workshop to determine the frame-by-frame coordinates. The end result should be two arrays containing the x- and y-coordinates of the object in each frame.

### Step 3: Build and Fit the Model

The motion of an object accelerating uniformly from rest is described by the following differential equation:

$$\frac{\mathrm{d}^2y}{\mathrm{d}t^2} = g$$

where $g$ is the acceleration of the object and $y(t)$ is the object's vertical position at time $t$. Integrating this equation results in an equation for the vertical position of the object:

$$y(t) = y_0 - \frac{1}{2}gt^2 $$

By plotting this curve against the experimental results determined in step 2, find the value of $g$ which best fits.

### Optional Extension Activities

To achieve the highest mark for this assessment, you should complete an extention activity which goes beyond the project goal. For example, you could use the techniques to measure another physical parameter (e.g. coefficient of friction) or perform error analysis to quantify the accuracy of your results. You can discuss your extension activity ideas with one of the tutors.

## Submission

You should submit your solution to the problem as a Jupyter Notebook, including code cells and Markdown. Your submission should include enough explanatory text that the reader can easily understand how you completed the experiment. See Moodle for the submission deadline and instructions.

## Mark Scheme

Each project group will be awarded a mark as follows.

|Grade|Class|Criterion|
| ---  | ---        |---|
|100%|Distinction|A solution to the problem which also goes beyond the project goal by completing an extension activity|
|70%|Merit|A solution to the problem which meets the project goal by correctly determining a value for $g$|
|39%|Fail|Failed to solve the problem or notebook does not run correctly|

