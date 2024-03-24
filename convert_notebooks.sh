# run this from the the top-level directory
# it creates there a notebooks/ and _solved/solutions/ dir
# that get automatically copied to the correct places


declare -a arr=(
                #"00-jupyter_introduction.ipynb"
                #"01-basic.ipynb"
                #"02-control_flow.ipynb"
                #"03-functions.ipynb"
                #"04-reusing_code.ipynb"
                #"05-numpy.ipynb"
                #"python_rehearsal"
                "00-jupyter_introduction.ipynb"
                "pandas_01_data_structures.ipynb"
                "pandas_02_basic_operations.ipynb"
                "pandas_03a_selecting_data.ipynb"
                "pandas_03b_indexing.ipynb"
                "pandas_04_time_series_data.ipynb"
                "pandas_05_groupby_operations.ipynb"
                "pandas_06_data_cleaning.ipynb"
                "pandas_07_missing_values.ipynb"
                "pandas_08_reshaping_data.ipynb"
                "pandas_09_combining_datasets.ipynb"
                "visualization_01_matplotlib.ipynb"
                "visualization_02_seaborn.ipynb"
                "visualization_03_landscape.ipynb"
                "case1_bike_count.ipynb"
                "case2_observations.ipynb"
                "case3_bacterial_resistance_lab_experiment"
                "case4_air_quality_processing.ipynb"
                "case4_air_quality_analysis.ipynb"
                )

cd _solved

mkdir ./notebooks

echo "- Converting notebooks"

for i in "${arr[@]}"
do
   echo "--" "$i"
   jupyter nbconvert --to=notebook --config ../nbconvert_config.py --output "notebooks/$i" "$i"
done

echo "- Copying converted notebooks and solutions"
cp -r notebooks/. ../notebooks
cp -r _solutions/. ../notebooks/_solutions

rm -r notebooks/
rm -r _solutions/

cd ..


declare -a arr=(
                "00-jupyterlab.ipynb"
                "01-variables.ipynb"
                "02-functions-use.ipynb"
                "03-containers.ipynb"
                "04-control-flow.ipynb"
                "05-functions-write.ipynb"
                )

cd _solved/python_intro

mkdir ./notebooks

echo "- Converting notebooks"

for i in "${arr[@]}"
do
   echo "--" "$i"
   jupyter nbconvert --to=notebook --config ../../nbconvert_config.py --output "notebooks/$i" "$i"
done



echo "- Copying converted notebooks and solutions"
cp -r notebooks/. ../../notebooks/python_intro
cp -r _solutions/. ../../notebooks/python_intro/_solutions

rm -r notebooks/
rm -r _solutions/

cd ../..


