import numpy as np

class EightQueens(object):
    '''
    classdocs
    '''

    def __init__(self, min_symbol,max_symbol,individual_size):
        '''
        Constructor
        '''
        self.max_symbol = max_symbol
        self.min_symbol = min_symbol
        self.individual_size = individual_size
        
    def initPopulation(self, num_individuals):
        
        num_individuals
        
        population = []
        #Cria todos os indiviudos e insere na populacao inicial
        for i in range(num_individuals):
            individual = np.random.random_integers(1, self.max_symbol,self.individual_size)
            population.append(individual.tolist())
        return population    
    
    def fitness(self,population):
    
        fitnessPop=[]
        #calculate the fitness for each individual of population
        for individual in population:
            fitnessPop.append(self.getFitness(individual))
    
        return fitnessPop
    
    def getIndividualSize(self):
        return self.individual_size
    
    def getMaxGeneSymbol(self):
        return self.max_symbol
    
    def getMinGeneSymbol(self):
        return self.min_symbol
    
    
    def getFitness(self,individual):
        
        fitness=0
        for j in range(self.individual_size-1):
            #.. and compare with each individual in all other positions
            for k in range(j+1,self.max_symbol):
                if (individual[j]!=individual[k]): # queens are not at the same line
                    if((individual[j]+(k-j))!=individual[k]): # queen are not at the same superior diagonal
                        if((individual[j]-(k-j))!=individual[k]): # queens are not at the same inferior diagonal
                            fitness=fitness+1; 
        return fitness
    
    def printSolution(self,solution):
        
        for i in range(self.individual_size):
            for j in range(self.individual_size):
                if i+1 == solution[j]:
                    output='Q '
                else:
                    output = '. '
                if j == self.individual_size-1:
                    print(output)
                else:
                    print(output),    