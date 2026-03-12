# Inventory Fundamentals – M1S1

## User Story M1S1
**Fundamentals and Basic Inventory Operations**

This project is a simple Python program that allows users to register a product in an inventory system and calculate its total cost. The objective is to practice fundamental programming concepts such as user input, variables, mathematical operations, error handling, and console output.

---

# Objective

The goal of this project is to:

- Register products with **name, price, and quantity**
- Calculate the **total cost of the product**
- Apply basic programming concepts such as:
  - User input
  - Variables
  - Mathematical operations
  - Error handling
  - Console output

---

# Tasks

## TASK 1 — Flowchart

A flowchart was created to represent the product registration process in the inventory.

Process:

Start → Read Product Name → Read Product Price → Read Product Quantity → Calculate Total Cost → Display Result → End

The flowchart was created using **draw.io** and exported as an image or PDF as evidence of the design.

---

## TASK 2 — Data Input (Python Variables)

A Python file called **inventario.py** was created.

The program asks the user to enter the following data:

- Product name → `string`
- Product price → `float`
- Product quantity → `int`

The program uses `input()` to request the data and converts numeric values using `float()` and `int()`.

If the user enters an invalid value, the program shows an error message and asks for the data again using `try/except`.

Example:

```python
name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Product Quantity: "))
