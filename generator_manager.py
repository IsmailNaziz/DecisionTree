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
        The target must be True or False
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

    def __init__(self, file_name, nb_columns, nb_rows=0, col_names=None, nb_cat=0, l_cat_values=None):
        self.file_name = file_name
        self.nb_columns = nb_columns
        self.nb_rows = nb_rows
        self.col_names = self._set_col_names(col_names)
        self.output_folder = r'..\DecisionTree\inputs'
        self.nb_cat = nb_cat
        self.l_cat_values = l_cat_values

    def _set_col_names(self, col_names):
        if col_names is None:
            return ['column {}'.format(i) for i in range(self.nb_columns)]
        elif len(col_names) != self.nb_columns:
            raise ValueError('Your col_name list should have the same size as the number of columns')

        return col_names

    def generate_random_cat_list(self, l_cat_values):
        """Generates a list of random values from l_cat_values list"""
        return random.choices(l_cat_values, k=self.nb_rows)

    def run(self):
        nb_num_cols = self.nb_columns - self.nb_cat  # number of numerical columns >= 0
        if nb_num_cols >= 0:
            df_num = pd.DataFrame(np.random.randint(0, 100, size=(self.nb_rows, nb_num_cols)))
            df_cat = pd.DataFrame(
                np.array([self.generate_random_cat_list(self.l_cat_values) for i in range(self.nb_cat)]) \
 \
                .reshape(self.nb_rows, self.nb_cat))

            df = pd.concat([df_num, df_cat], axis=1)
            df.columns = self.col_names
            df['target'] = random.choices(['True', 'False'], k=self.nb_rows)
            os.makedirs(self.output_folder, exist_ok=True)
            df.to_csv('{}/{}'.format(self.output_folder, self.file_name), index=False)
        else:
            raise ValueError('The number of categorical columns must be less or equal the number of columns')


if __name__ == '__main__':
    parameters_set = {'file_name': 'data', 'nb_columns': 3, 'nb_rows': 10, 'nb_cat': 1, 'col_names': list('abc'),
                      'l_cat_values': ['Agadir', 'Paris', 'Ananas']
                      }
    GM = GeneratorManager(**parameters_set)
    GM.run()
