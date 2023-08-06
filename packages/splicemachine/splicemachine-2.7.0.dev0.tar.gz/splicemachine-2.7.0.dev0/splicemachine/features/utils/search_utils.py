from splicemachine.spark.utils import spark_df_size
import pandas as pd
from ipywidgets import widgets, Layout, interact
from IPython.display import display, clear_output
import pandas_profiling, spark_df_profiling
import re


def feature_search_internal(fs, pandas_profile=True):
    """
    The internal (Splice managed notebooks) feature search for the Splice Machine Feature Store
    """
    from beakerx import TableDisplay
    from beakerx.object import beakerx
    beakerx.pandas_display_table()
    print('Filter on Feature name, tags, attributes, or feature set name. Search multiple values with "&" and "|" Enter a single Feature name for a detailed report. ')
    pdf = fs.get_features_by_name()
    pdf = pdf[['name', 'feature_type', 'feature_data_type', 'description','feature_set_name','tags','attributes','last_update_ts','last_update_username','compliance_level']]

    ############################################################################################
    searchText = widgets.Text(layout=Layout(width='80%'), description='Search:')
    display(searchText)

    def handle_submit(sender):
        res_df = pdf
        # Add an & at the beginning because the first word is exclusize
        ops = ['&'] + [i for i in searchText.value if i in ('&','|')] # Need to know if each one is an "and" or an "or"
        for op,word in zip(ops, re.split('\\&|\\|',searchText.value)):
            word = word.strip()
            temp_df = pdf[pdf['name'].str.contains(word, case=False) | pdf['tags'].astype('str').str.contains(word, case=False, regex=False) | pdf['attributes'].astype('str').str.contains(word, case=False, regex=False) | pdf['feature_set_name'].str.contains(word, case=False, regex=False)]
            res_df = pd.concat([res_df, temp_df]) if op=='|' else res_df[res_df.name.isin(temp_df.name)]

        res_df.reset_index(drop=True, inplace=True)
        table = TableDisplay(res_df)
        redisplay(table)

    searchText.on_submit(handle_submit)

    def on_feature_select( row, col, tabledisplay):
        redisplay(tabledisplay)
        feature_name = tabledisplay.values[row][0]
        print('Generating Data Report...')
        data = fs.get_training_set([feature_name], current_values_only=True).cache()
        if pandas_profile:
            df_size = spark_df_size(data)
            print('Gathering data')
            if df_size >= 5e8: # It's too big for pandas
                print("Dataset is too large. Profiling with Spark instead")
                display(spark_df_profiling.ProfileReport(data.cache(), explorative=False))
            else:
                print('Profiling Data')
                display(pandas_profiling.ProfileReport(data.toPandas(), explorative=False))
        else:
            print('Profiling Data')
            display(spark_df_profiling.ProfileReport(data, explorative=True))

    def redisplay(td):
        clear_output(wait=True)
        display(searchText)
        td.setDoubleClickAction(on_feature_select)
#         td.setColumnFrozen('name',True)
        display(td)


    table_data=pdf
    table = TableDisplay(table_data)
    redisplay(table)


def feature_search_external(fs, pandas_profile=True):
    """
    The external (Not Splice managed notebooks) feature search for the Splice Machine Feature Store

    :param pandas_profile: If you want to run feature level profiling with Pandas or Spark. If pandas is set to True,
        but the size of the Feature data is too large, it will fall back to spark
    """

    pdf = fs.get_features_by_name()
    @interact
    def column_search(Filter=''):
        display_cols = ['name', 'feature_type', 'feature_data_type', 'description','feature_set_name','tags','attributes','last_update_ts','last_update_username','compliance_level']
        print('Filter on Feature name, tags, attributes, or feature set name. Search multiple values with "&" and "|" Enter a single Feature name for a detailed report. ')
        res_df = pdf
        # Add an & at the beginning because the first word is exclusize
        ops = ['&'] + [i for i in Filter if i in ('&','|')] # Need to know if each one is an "and" or an "or"
        for op,word in zip(ops, re.split('\\&|\\|',Filter)):
            word = word.strip()
            temp_df = pdf[pdf['name'].str.contains(word, case=False) | pdf['tags'].astype('str').str.contains(word, case=False, regex=False) | pdf['attributes'].astype('str').str.contains(word, case=False, regex=False) | pdf['feature_set_name'].str.contains(word, case=False, regex=False)]
            res_df = pd.concat([res_df, temp_df]) if op=='|' else res_df[res_df.name.isin(temp_df.name)]
        res_df.reset_index(drop=True, inplace=True)
        res_df = res_df[display_cols]
        if len(res_df) == 1:
            print("Generating Report...")
            col_name = res_df['name'].values[0]
            print(col_name)
            data = fs.get_training_set([col_name], current_values_only=True).cache()
            print('Gathering data')
            df_size = spark_df_size(data)
            print('Profiling Data')
            if pandas_profile:
                if df_size >= 5e8: # It's too big for pandas
                    print("Dataset is too large. Profiling with Spark instead")
                    display(spark_df_profiling.ProfileReport(data.cache(), explorative=True))
                else:
                    display(pandas_profiling.ProfileReport(data.toPandas(), explorative=True))
            else:
                display(spark_df_profiling.ProfileReport(data.cache(), explorative=True))
        return res_df
