#jupyter nbconvert --to=notebook --config nbconvert_config.py --output "02 - Data structures.ipynb" "solved - 02 - Data structures.ipynb" 
# jupyter nbconvert --to=notebook --output "03b - Some more advanced indexing.ipynb" "solved - 03b - Some more advanced indexing.ipynb"
#jupyter nbconvert --to=notebook --config nbconvert_config.py --output "03 - Indexing and selecting data.ipynb" "solved - 03 - Indexing and selecting data.ipynb"
#jupyter nbconvert --to=notebook --config nbconvert_config.py --output "04 - Groupby operations.ipynb" "solved - 04 - Groupby operations.ipynb"


#jupyter nbconvert --to=notebook --config nbconvert_config.py --output "04b - Advanced groupby operations.ipynb" "_solved/"
#jupyter nbconvert --to=notebook --config nbconvert_config.py --output "05 - Time series data.ipynb" "solved - 05 - Time series data.ipynb"
#jupyter nbconvert --to=notebook --config nbconvert_config.py --output "06 - Reshaping data.ipynb" "solved - 06 - Reshaping data.ipynb"


declare -a arr=(
                #"00-jupyter_introduction.ipynb"
                #"01-basic.ipynb"
                #"02-control_flow.ipynb"
                #"03-functions.ipynb"
                #"04-reusing_code.ipynb"
                #"05-numpy.ipynb"
                #"python_rehearsal"
                #"pandas_01_data_structures.ipynb"
                #"pandas_02_basic_operations.ipynb" 
                #"pandas_03_selecting_data.ipynb"
                #"pandas_04_time_series_data.ipynb"
                "pandas_05_combining_datasets.ipynb"
                "pandas_06_groupby_operations.ipynb"
                "pandas_07_reshaping_data.ipynb"
                #"case1_bike_count.ipynb"
                "case2_biodiversity_cleaning.ipynb"
                "case2_biodiversity_analysis.ipynb"
                )


for i in "${arr[@]}"
do
   echo "$i"
   # or do whatever with individual element of the array
   
   jupyter nbconvert --to=notebook --config ../nbconvert_config.py --output "notebooks/$i" "$i"   
done
