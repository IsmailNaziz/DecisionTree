import pandas as pd
import numpy as np
from node import Node


class DecisionTreeEngine(object):

    def __init__(self, max_depth):
        # self.file_name = file_name
        # self.df = self._read_file()
        # self.cost_function = cost_function
        # self.df_description = self._set_description_df()
        self.max_depth = max_depth

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
        return df[df["output"] == True & df["input"] == True], df[df["output"] == True & df["input"] == False], \
               df[df["output"] == False & df["input"] == True], df[df["output"] == False & df["input"] == False]

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

    def select_best_split(self, x, y):
        """ALL COLUMNS + GINI
        return threshold + col or col"""
        if y.size <= 1:
            return None, None
        best_feature, best_threshold = None, None
        best_gini = self.gini(y)
        for col in x.columns:
            sorted_samples, classes = zip(*sorted(zip(x[col], y)))
            classes = pd.DataFrame(classes)
            # print('best threshold: {} best gini {}'.format(best_threshold, best_gini))
            for i in range(1, len(sorted_samples)):
                gini_left = self.gini(classes[:i])
                gini_right = self.gini(classes[i:])
                gini = (classes[:i].size / y.size) * gini_left + (classes[i:].size / y.size) * gini_right

                if gini < best_gini:
                    best_gini = gini
                    print('gini= ', best_gini)
                    best_feature = col
                    best_threshold = (sorted_samples[i - 1] + sorted_samples[i]) / 2

        # print('best threshold: {} best gini {}'.format(best_threshold, best_gini))
        return best_feature, best_threshold

    def calculate_cost(self, df, input_col, output_col):
        dft = df[[input_col, output_col]]
        dft.rename(columns={input_col: "input", output_col: "output"})
        if self.df_description[input_col] == 'continuous':
            return
        elif self.df_description[input_col] == 'categortcal':
            return

    def gini(self, y):

        return 1 - ((y.value_counts() / y.shape[0]) ** 2).sum()

    def calculate_lowest_cost(self):
        return

    def generate_tree(self, x, y, depth=0):
        '''

        :param depth:
        :param df: input data
        :return: tree
        '''

        node = Node()
        if depth <= self.max_depth:
            feature, tr = self.select_best_split(x, y)
            if feature is not None:
                node.feature = feature
                node.threshold = tr
                df = pd.concat([x, y], axis=1)
                df_left = df[df[feature] <= tr]
                df_right = df[df[feature] > tr]
                node.left = self.generate_tree(df_left[x.columns], df_left['target'], depth=depth + 1)
                node.right = self.generate_tree(df_right[x.columns], df_right['target'], depth=depth + 1)
        return node

    def fit(self, x, y):

        self.tree = self.generate_tree(x, y)


    def predict(self, x):
        tree = self.tree
        while tree.left:
            if x[tree.feature] <= tree.threshold:
                tree = tree.left
            else:
                tree = tree.right
        return tree.predicted_class


if __name__ == '__main__':
    clf = DecisionTreeEngine(max_depth=50)
    df = pd.DataFrame({
        'A': [5, 7, 7, 9, 12, 91, 5, 3553, 1, 365],
        'B': [11, 7, 80, 100, 13, 13, 11, 10, 154, 1155],
        'target': [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]})
    y = df['target']
    x = df.drop(['target'], axis=1)
    clf.fit(x, y)
    print(clf.select_best_split(x, y))

