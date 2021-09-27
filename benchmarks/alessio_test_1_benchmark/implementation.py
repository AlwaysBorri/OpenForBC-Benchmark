from common.benchmark_wrapper import BenchmarkWrapper
import json
import os

import torch 

class Alessio1Benchmark(BenchmarkWrapper): #it's the same class inside benchmark_info.json

    def __init__(self):
        self.filePath = os.path.dirname(__file__) #os.path.dirname(__file__) returns the path of this file
        
    

    def setSettings(self, settings_file):
        """
        Open and read the settings file
        """
        settings = os.path.join(self.filePath, "settings", settings_file)
        self.dimension1 = json.load(open(settings, "r"))["dimension1"]
        self.dimension2 = json.load(open(settings, "r"))["dimension2"]

    
    def startBenchmark(self, verbosity=None):
        
        print("The first dimension of the matrix is equal to", self.dimension1)
        print("The second dimension of the matrix is equal to", self.dimension2)

        matrix_1 = torch.randn(self.dimension1, self.dimension2)
        matrix_2 = torch.randn(self.dimension1, self.dimension2)

        product = torch.tensordot(matrix_1, matrix_2)

        print("The shape of the product matrix is", product.size())
    
        return {"output": product} #Where does this output go?

    
    def benchmarkStatus():
        pass


    def getSettings(self):
        pass

    def stopBenchmark():
        pass
