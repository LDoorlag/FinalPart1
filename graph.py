import matplotlib.pyplot as plt

class Graph:
    '''
    Generates the graph for the votes
    '''
    def __init__(self):
        '''
        gathers the data from the text file for to prep for graphing
        '''
        with open("votes.txt", "r") as file:
            self.Jane = "Jane"
            self.John = "John"
            self.JaneVotes = 0
            self.JohnVotes = 0
            for line in file:
                line = line.split()
                if line[1] == "1":
                    self.JohnVotes += 1
                else:
                    self.JaneVotes += 1
        
    def plot(self):
        '''
        creates graph based on data gathered during init
        param: None
        return: None
        '''
        plt.bar([self.Jane, self.John], [self.JaneVotes, self.JohnVotes])
        plt.xlabel("Candidates")
        plt.ylabel("Votes")
        plt.title("Votes for Candidates")
        plt.show()
if '__main__' == __name__:
    Graph().plot()
