# run this from the _solved directory
# it creates there a notebooks/ and _solutions/ dir
# then manually copy this to the ../notebooks dir


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
                #"pandas_05_combining_datasets.ipynb"
                #"pandas_06_groupby_operations.ipynb"
                #"pandas_07_reshaping_data.ipynb"
                #"visualization_01_matplotlib.ipynb"
                #"visualization_02_plotnine.ipynb"
                "visualization_03_landscape.ipynb"
                #"case1_bike_count.ipynb"
                #"case2_biodiversity_processing.ipynb"
                #"case2_biodiversity_analysis.ipynb"
                #"case3_bacterial_resistance_lab_experiment"

                #"case4_air_quality_processing.ipynb"
                #"case4_air_quality_analysis.ipynb"
                "case4_air_quality_processing.ipynb"
                "case4_air_quality_analysis.ipynb"
                )


for i in "${arr[@]}"
do
   echo "$i"
   # or do whatever with individual element of the array
   
   jupyter nbconvert --to=notebook --config ../nbconvert_config.py --output "notebooks/$i" "$i"   
done
