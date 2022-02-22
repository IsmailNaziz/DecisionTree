import os
import random
import numpy as np
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
    def __init__(self, file_name, nb_columns, nb_rows=0, col_names=None):
        self.file_name = file_name
        self.nb_columns = nb_columns
        self.nb_rows = nb_rows
        self.col_names = self._set_col_names(col_names)
        self.output_folder = r'..\DecisionTree\inputs'

    def _set_col_names(self, col_names):
        if col_names is None:
            return ['column {}'.format(i) for i in range(self.nb_columns)]
        elif len(col_names) != self.nb_columns:
            raise ValueError('Your col_name list should have the same size as the number of columns')
        
        return col_names

    def run(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(self.nb_rows, self.nb_columns)), columns=self.col_names)
        os.makedirs(self.output_folder, exist_ok=True)
        df.to_csv('{}/{}'.format(self.output_folder, self.file_name))


if __name__=='__main__':
    parameters_set = {'file_name': 'out', 'nb_columns': 3, 'nb_rows': 10}
    GM = GeneratorManager(**parameters_set)
    GM.run()
