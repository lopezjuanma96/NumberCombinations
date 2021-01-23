# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:32:54 2021

@author: Juanma
"""

import numpy as np
import tkinter as tk

#Functions

def all_permutations(array):
    
    #When array has only one object we done permute
    if array.shape[0] == 1:
        return array
    
    #This list will store the different permutations in each level of recurrency
    l = []
    #If array is bigger than one
    for i in range(array.shape[0]):
        
        first = array[i]
        remain = np.append(array[:i], array[i+1:])
        for p in all_permutations(remain): #Here we recur the function but with the remaining
            l.append(np.append(first, p))
    
    return l

def all_combinations(array, size):
    
    full_list = []
    base = array.shape[0]
    
    for comb in range(base**size):
        comb_list = []
        dividend = comb
        
        while True:
            comb_list.append(array[dividend % base])
            dividend = dividend // base
            if dividend <= 0: #this simulate a "do while" loop in Python because I want the loop to stop when dividend is 0 but the first time that the dividend STARTS at 0 I want it to run the loop once
                break
            
        while len(comb_list) < size:
            comb_list.append(array[0])
        
        full_list.append(np.array(comb_list))
    
    return np.array(full_list)

def plus(a,b):
    return a + b

def dif(a,b):
    return a - b

def prod(a,b):
    return a * b

def div(a,b):
    return a / b

#classes

class GameParams:
    
    operations = {"+" : plus,
                  "-" : dif,
                  "x" : prod,
                  "/" : div}
    
    def __init__(self, no_operands = 4, operand_limits = [1,10], set_case = False, operands_to_set = None, result_to_set = None):
        self.no_operands = no_operands
        self.operand_limits = operand_limits
        
        if set_case:
            if operands_to_set is not None and result_to_set is not None:
                self.operands = np.array(operands_to_set)
                self.result = np.array(result_to_set)
                self.random = np.array(operands_to_set + result_to_set)
                self.no_operands = len(operands_to_set)
            else:
                raise ValueError ("You must input the operands_to_set and result_to_set if set_case is True")
        else:
            self.random = np.random.randint(operand_limits[0], operand_limits[1], size = no_operands + 1)
        
        self.operands = self.random[:-1]
        self.fixed_operands = self.operands.copy()
        self.result = self.random[-1]

        self.has_solution = False
        self.solution_array = []        

    def compute(self):
        
        solved = False
        no_operations = self.no_operands - 1
        op_combinations = all_combinations(np.array(list(self.operations.keys())), 
                                           no_operations)
        
        for comb in op_combinations:
            part_op_symbols = []
            part_op = []
            for op in comb:
                part_op_symbols.append(op)
                part_op.append(self.operations[op])
                
            solution_string = str(self.operands[0])
            part_result = self.operands[0]
            for j in range(no_operations):
                part_result = part_op[j](part_result, self.operands[j+1])
                solution_string = solution_string + " " + part_op_symbols[j] + " " + str(self.operands[j+1])
            solution_string = solution_string + " = " + str(self.result)
                
            if part_result == self.result:
                self.solution_array.append(solution_string)
                solved = True
                break
                        
        if solved:
            self.has_solution = True
            
    def attempt(self):
        for p in all_permutations(self.fixed_operands):
            self.operands = p
            self.compute()
        
    def print_quiz(self):
        operands_to_print = ""
        for op in range(self.no_operands):
            if op == self.no_operands - 1: #if its the last one
                operands_to_print = operands_to_print + str(self.fixed_operands[op])
            elif op == self.no_operands - 2: #if it's the second to last one
                operands_to_print = operands_to_print + str(self.fixed_operands[op]) + " & "
            else:
                operands_to_print = operands_to_print + str(self.fixed_operands[op]) + ", "
    
        result_to_print = str(self.result)
        
        print("How can you combine: " + operands_to_print + " to get " + result_to_print)
    
    def print_solution(self):
        if self.has_solution:
            for s in self.solution_array:
                print(s)
                
        else:
            print(self.fixed_operands, " can't be combined to get ", self.result)

try:
    game = GameParams(no_operands = 2)
    game.print_quiz()
    game.attempt()
    while True:
        if not game.has_solution:
            game = GameParams(no_operands = 2)
            game.print_quiz()
            game.attempt()

except KeyboardInterrupt:
    
    game.print_solution() 

"""
To complete:
    
    - Use DearPyGUI or Tkinter for a User Interface
"""

