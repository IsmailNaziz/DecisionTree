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
    pass

if __name__=='__main__':
    parameters_set = {}
    GM = GeneratorManager(**parameters_set)
    GM.run()