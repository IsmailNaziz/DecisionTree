import pandas as pd
import numpy as np
class DecisionTreeEngine(object):

    def __init__(self, file_name, cost_function):
        self.file_name = file_name
        self.df = self._read_file()
        self.cost_function = cost_function
        self.df_description = self._set_description_df()

    def _set_description_df(self):
        ''' return dict keys:col_name value type, it can be either continuous, categorical'''
        return

    def _read_file(self):
        ''' Temp function for the moment waiting for input manager to be coded'''
        return

    def split(self, df):
        '''TO DO: change the name'''
        return df[df["output"]==True & df["input"]==True], df[df["output"]==True & df["input"]==False],\
                df[df["output"] == False & df["input"] == True], df[df["output"]==False & df["input"]==False]

    def general_probability(self, df):
        ''' general case when input and output are both True or False '''
        df_IT_OT, df_IF_OT, df_IT_OF, df_IF_OF = self.split(df)
        return

    def convert_input_to_boolean(self):
        return

    def calculate_cost(self, df, input_col, output_col):
        dft = df[[input_col, output_col]]
        dft.rename(columns={input_col: "input", output_col: "output"})
        if self.df_description[input_col] == 'continuous':
            return
        elif self.df_description[input_col] == 'categortcal':
            return
    def gini(self, ps):
        '''calculates gini function
        input: - ps an object of type pandas Series over which we want to compute gini function
        output:- gini index value
        '''
        if isinstance(ps,pd.Series):
            p=ps.value_counts()/len(ps)
            return 1- np.sum(p**2)
        else:
            raise('the object must be a pandas Series ')



    def calculate_lowest_cost(self):
        return