"""Defines the Student Workload Calculator class"""
class StudentWorkloadCalculator:
    def __init__(self):
        self._classHours = 20
        self._workHours = 10

    def getClassHours(self):
        return self._classHours
    
    def setClassHours(self, newClassHours):
        self._classHours = newClassHours

    def getWorkHours(self):
        return self._workHours
    
    def setWorkHours(self, newWorkHours):
        self._workHours = newWorkHours
    
    def getIndepStudyHours(self):
        return self._classHours * 2
    
    def calculateWorkload(self):
        return self._classHours + self.getIndepStudyHours() + self._workHours

    