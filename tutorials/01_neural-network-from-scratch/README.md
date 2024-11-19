# Building a Neural Network from Scratch: A Comprehensive Guide

## Script Description

This Python script demonstrates how to build a simple neural network from scratch using **NumPy**. It uses a small customer dataset to predict whether a customer will buy a product based on their income and time spent on a website. The script covers the steps of forward and backward propagation, loss computation, and parameter updates using gradient descent. At the end of training, the loss over epochs is plotted, and the network provides binary predictions (0 = No, 1 = Yes) for each customer.

## How to Run the Script

1. **Install dependencies**: Ensure you have the required Python libraries installed:
   ```bash
   pip install numpy matplotlib
   ```
2. **Run the script**: Execute the script from the command line or your preferred IDE:
   ```bash
   python script.py
   ```
3. **View results**: The script visualizes the training loss over epochs and outputs the model's predictions for the customer dataset.

## Results ##
+ **Training Loss**: The loss is plotted over the epochs to track the model’s learning progress.
+ **Predictions**: The final output will display the predictions (0 or 1) for each customer.

## Conclusion ##
This tutorial demonstrates the basics of building a neural network from scratch. By implementing the forward and backward propagation manually, you can better understand how neural networks work internally. For more advanced applications, consider using frameworks like TensorFlow or PyTorch.