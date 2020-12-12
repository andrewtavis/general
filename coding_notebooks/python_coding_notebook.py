# =============================================================================
# Python Coding Notebook
#
# Useful code snipits and things that have been stack overflowed too many times
# =============================================================================

import pandas as pd
import coding_notebooks.python_coding_notebook

def remove_col_if_in(df, col):
    """
    Checks for a column and removes it if present
    """
    if str(col) in list(df.columns):
        df.drop(str(col), axis=1, inplace=True)
        print(df.shape[1])


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


def gen_list_of_lists(original_list, new_structure):
    """Generates a list of lists with a given structure from a given list"""
    assert len(original_list) == sum(new_structure), \
    "The number of elements in the original list and desired structure don't match"

    list_of_lists = [[original_list[i + sum(new_structure[:j])] for i in range(new_structure[j])] \
                     for j in range(len(new_structure))]

    return list_of_lists


"""
df.loc[row, col] # col is str

df[df.loc[row, col]]
"""


"""
df.iloc[row, col] # col is int

df[df.iloc[row, col]]
"""


"""
df.drop(i, inplace=True)
df = df.drop(i, inplace=False)
"""


"""
df.pivot_table(values=['column_1', 'column_2'],
               index='column_3',
               aggfunc=[np.mean], # np.sum
               margins=True)
"""


"""
Figure axis organization
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(20,5))

fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2, sharey=True, figsize=(20,5))

fig, [ax1, ax2, ax3, ax4] = plt.subplots(nrows=4, ncols=1, sharey=True, figsize=(20,40))
"""


"""
Sort list and return original list indexes in sorted order
[tup[0] for tup in sorted(enumerate(list), key=lambda i:i[1])]
"""

"""
Sort a dictionary by values
{k: v for k, v in sorted(a_dict.items(), key=lambda item: item[1])[::-1]}
"""

"""
Column assignment
df.loc[:,'col'] = pd.Series([1,2,3], index=df.index)
"""


"""
Subset based on two column values
df[(df['col1'] == x) & (df['col2'] > y)] # needs to be & instead of and, as & returns a boolean array
"""


"""
Flatten a list of lists
flat_list = [item for sublist in list_of_lists for item in sublist]
-----
from pandas.core.common import flatten
list(flatten(l))
-----
import itertools
flatten = itertools.chain.from_iterable
list(flatten(l))
"""


"""
Shuffle only part of a list
list[x:y] = random.sample(list[x:y], len(list[x:y]))

list[another_list.index(x):another_list.index(y)] = random.sample(list[another_list.index(x):another_list.index(y)], len(another_list))
"""


"""
Insert into list by index:
new_list = list[:].insert(item, index)
---
new_list = list[:]
new_list[index:index] = [item]
"""


"""
Reindex a df
df.reset_index(drop=True, inplace=True)
"""


"""
Insert column into df at an index
"""


"""
Change Seaborn Colors:
https://seaborn.pydata.org/tutorial/color_palettes.html

sns.set_palette("deep") # default

random_rgba = (random.random(), random.random(), random.random(), random.random())

colors = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.palplot(sns.color_palette(colors))
sns.set_palette(colors)
"""


"""
# pylint: disable=unused-variable
"""


"""
Adding data to the top of vertical barplot bars
for p in ax.patches:
    ax.text(x = p.get_x() + p.get_width() / 2.0,
            y = p.get_height() + 1,
            s = str(p.get_height()),
            ha = "center")

Adding data to the right of horizontal barplot bars
for p in ax.patches:
    ax.text(x = p.get_width() + 1,
            y = p.get_y() + p.get_height() / 2,
            s = str(p.get_width()),
            ha = "center")
"""


"""
Subsetting a df based on more than one option for a column
df.loc[df['column_name'].isin(some_values)]
"""


"""
Subsetting a df based on options for more than one column
df[(df['col_1'] == val_1) & (df['col_2'] == val_2)]
"""

"""
Add timestamp to filename

import time
timestr = time.strftime("%Y%m%d-%H%M%S")

'{}'.format(timestr)
"""

"""
Replace value in list
list = [i.replace(old, new) for i in list]
"""

"""
Subset df by list of values
df = df[df.column.isin(list_of_vals)]

df = df[~df.column.isin(list_of_vals)]
"""

"""
Rotate x-axis ticks
plt.xticks(rotation=45)
"""

"""
Value counts for items within a list of lists
from collections import Counter
Counter(i for l in list_of_lists for i in l)
"""


"""
Combine list values into a string
''.join([word for word in flat_words])
"""

"""
Order dictionary by values
{k: v for k, v in sorted(a_dict.items(), key=lambda item: item[1])}
"""