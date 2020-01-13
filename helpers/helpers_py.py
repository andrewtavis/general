# =============================================================================
# Helper functions for Python
# 
# Contents:
# 1. Environment
#   1.1 in_ipynb
#   1.2 dev_import
#
# 2. Dataframes
#   2.1 head_shape
#   2.2 remove_col_if_in
# 
# 3. Time
#   3.1 remove_timezone
#   3.2 convert_epoch_dt
# =============================================================================

import helpers_py

# =============================================================================
# 1. Environment
# =============================================================================

def in_ipynb():
    """
    Checks if the current environment is an iPython notebook, changing functional actions if so

    Dependent for
    -------------
        head_shape : for display or print actions
    """
    try:
        cfg = get_ipython().config 
        if cfg['IPKernelApp']:
            return True
        else:
            return False
    except NameError:
        return False


def dev_import(package_name):
    """
    Checks for a local package file for import, and imports the global version if not present
    """
    try:
        from . import package_name
        print('Local version of {} found - importing for development'.format(str(package_name)))
    except:
        import package_name
        print('No local version of {} found - importing from the global Python environment'.format(str(package_name)))


# =============================================================================
# 2. Dataframes
# =============================================================================

def head_shape(df, head_count=5):
    """
    Displays or prints the head of a df given the environment

    Dependent on
    ------------
        in_ipynb : for environment derivation
    """
    if helpers_py.in_ipynb():
        from IPython.display import display
        display(df.head(head_count))
        display(df.shape)
    else:
        print(df.head(head_count))
        print(df.shape)


def remove_col_if_in(df, col):
    """
    Checks for a column and removes it if present
    """
    if str(col) in list(df.columns):
        df.drop(str(col), axis=1, inplace=True)
        print(df.shape[1])


# =============================================================================
# 3. Time
# =============================================================================

def remove_timezone(df, col):
    """
    Removes timeszones from a given column
    """
    df[str(col)] = df[str(col)].apply(lambda x: x.replace(tzinfo=None))


def convert_epoch_dt(df, col):
    """
    Converts a column from epoch to datetime or vice versa
    """
    if df[str(col)].dtypes == '<M8[ns]':
        df[str(col)] = df[str(col)].astype('int64')
        print(df[str(col)].dtypes)
        print("Column {} converted to epoch".format(str(col)))
        return df[str(col)]

    elif df[str(col)].dtypes == 'int64':
        import pandas as pd
        df[str(col)] = pd.to_datetime(df[str(col)], errors="coerce")
        print(df[str(col)].dtypes)
        print("Column {} converted to datetime".format(str(col)))
        return df[str(col)]
    
    elif TypeError:
        print('Inappropriate arguments provided - check df and column types')