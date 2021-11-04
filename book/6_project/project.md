# Computing Project
For the rest of this course you will put together the concepts and skills you have learnt so far in order to conduct a simple (but genuine) scientific experiment.

## Introduction

It is well known that the value of [acceleration due to gravity at the Earth's surface (g)](https://en.wikipedia.org/wiki/Gravity_of_Earth) is approximately $8.91~\mathrm{m}/\mathrm{s}^2$. But how accurately can you measure the value of this physical constant using just a handheld video camera and your nascent programming skills?

:::{admonition} Project Goal
:class: tip
Perform an experiment to determine an estimate of the value of g. Use a handheld camera to capture the experimental results and Python to perform the analysis.
:::

## Step 1: Conduct an Experiment

Using a handheld video camera (e.g. the one in your smartphone), record the motion of an object falling vertically from rest. You can use any object you like, but I advise against anything breakable or expensive. You might need to experiment a little to determine a setup which reliably gives a clean and accurate recording, but don't spend a lot of time tinkering; you can refine the experiment later! The output of this step should be a movie file (e.g. `.mov` or `.avi`).

## Step 2: Extract the Data

Extract the data from the recording in the form of a sequence of x and y co-ordinates for each frame.
First you will need to upload the movie file. Then you can use the image manipulation library studied in the last workshop to determine the co-ordinates, but you will need to do this frame-by-frame. The code to extract the frame-by-frame image data from the video file is somewhat painful so I have provided it at the end of this document. The end result should be two arrays `x` and `y` containing the position of the object in each frame.

## Step 3: Build and Fit the Model

The motion of a uniformly accelerating object is described by the following differential equation:

$$\frac{d^2y}{dt^2} = a$$

where $a$ is the acceleration of the object and $y(t)$ is the object's vertical position at time $t$. Integrating this equation results in an equation for the vertical position of the object:

$$y(t) = y_0 - \frac{1}{2}at^2 $$

By plotting this curve against the experimental results determined in step 2, find the value of $a$ which best fits.
