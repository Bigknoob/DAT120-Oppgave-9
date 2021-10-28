# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:39:44 2021

@author: William test 123 test 
"""


class QuestionGame:
    def __init__(self, question, qanswer_op, correctanswer):
        self.question = question
        self.qanswer_op = qanswer_op
        self.correctanswer = correctanswer
        

    def correct_answer(self, answer):
        if answer == self.correctanswer:
            print("\nThat is correct!\n")
        else:
            print("\nThat is wrong!\n")
            
    def __str__(self):       
        answerstring = ""
        for y in range(len(self.qanswer_op)):
            answerstring += f"{y+1}. {self.qanswer_op[y]} \n"
        return f"{self.question} \n{answerstring}"
        
        
if __name__ == "__main__":
    q = QuestionGame("What is the biggest number?", ["12", "69", "33", "420"], 4)
    print(q)
    answer = int(input("What is the answer? "))
    q.correct_answer(answer)
    q10 = QuestionGame("What color is the sky?", ["Blue", "Red", "Green"], 1)
    print(q10)
    answer10 = int(input("What is the answer?"))
    q10.correct_answer(answer10)