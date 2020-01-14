# =============================================================================
# Helper functions for Python
# 
# Contents
# --------
#   1. Environment
#       in_ipynb
#
#   2. Dataframes - Display and Dimensions
#       head_shape
#       remove_col_if_in
# 
#   3. Dataframes - Time
#       remove_timezone
#       convert_epoch_dt
# =============================================================================

import helpers.helpers_py

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


# =============================================================================
# 2. Dataframes - Display and Dimensions
# =============================================================================

def head_shape(df, head_count=5):
    """
    Displays or prints the head of a df given the environment

    Dependent on
    ------------
        in_ipynb : for environment derivation
    """
    if helpers.helpers_py.in_ipynb():
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
# 3. Dataframs - Time
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