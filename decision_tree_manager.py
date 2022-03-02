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
        ''' Temp function for the moment, read csv '''
        return

    def split(self, df):
        '''TO DO: change the name,
        input df supposed to be compoesed of 2 columns input and output that are both boolean
        return 4 df splitted depending on booleans
        '''
        return df[df["output"]==True & df["input"]==True], df[df["output"]==True & df["input"]==False],\
                df[df["output"] == False & df["input"] == True], df[df["output"]==False & df["input"]==False]

    def calculate_gini_for_boolean_cols(self, df):
        ''' general case when input and output are both True or False
         calculate gini
         (case positive output, case ngative output, weighted with the number of samples'''
        df_IT_OT, df_IF_OT, df_IT_OF, df_IF_OF = self.split(df)
        return

    def convert_input_to_boolean(self):
        '''
        '''
        return

    def calculate_gini_for_continuous_cols(self):
        '''
        It is encouraged to use as many auxilairy methods as possible for the code to be clear
        this function uses self.df for calculation as input
        it outputs, dic composed of :
        dic = {'continuous col': {'tresh_hold': t, best_gini_associated_with_t: float}}
        It is encouraged an object to replace the nested dicts
        assumption: general_probability is coded
        '''
        return

    def select_best_split(self):
        '''ALL COLUMNS + GINI
        return threshhold + col or col'''
        return

    def calculate_cost(self, df, input_col, output_col):
        dft = df[[input_col, output_col]]
        dft.rename(columns={input_col: "input", output_col: "output"})
        if self.df_description[input_col] == 'continuous':
            return
        elif self.df_description[input_col] == 'categortcal':
            return

    def gini(self, p_x, p_y):
        return



    def calculate_lowest_cost(self):
        return