import os
import pandas as pd
class GeneratorManager(object):
    '''
    Features:
        file/folder management
        files generation
    Explanation:
        This class must create a folder for input storage
        This class must generate files with appropriate names
        The file generated must be a csv file
        Columns can be either categorical or continuous values
        The output must be True or False
        The user can provide, if he wants, the name of the columns
        The user can input number of rows
        The user can specify the number of column
        Default parameters have to be decided by the developer and be reasonable
        Only one csv
        ========================================================================
        Bonus:
        ** multiple csv
        ** The user can select/provide the distribution for continuous variable (ex: provide a distribution as input)
        ** The user can provide the categorical variables and the number occurrence of each one in a column
        ** The output can be a csv or a json or any table like output

    you need to implement the method run()
    '''
    def __init__(self,csv_name,n_columns):
        self.csv_name=csv_name
        self.n_columns=n_columns
        self.col_names=['column {}'.format(i) for i in range(self.n_columns)]
    def set_col_names(self, col_names):
        self.col_names=col_names
    def run(self):
        self.set_col_names(self.col_names)
        df = pd.DataFrame(columns=self.col_names)
        os.makedirs('..\DecisionTree\inputs', exist_ok=True)
        df.to_csv('..\DecisionTree\inputs\ '+self.csv_name)

        return




if __name__=='__main__':
    parameters_set = {'csv_name':'out','n_columns':3}
    GM = GeneratorManager(**parameters_set)
    GM.run()