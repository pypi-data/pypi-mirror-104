CUR_DIR=$(cd .. && pwd)
DATASET_DIR=$CUR_DIR/datasets/$1/
python3 ../application/mlexports.py $CUR_DIR -name=$1 -train=$DATASET_DIR/"$1"_TRAIN.arff -test=$DATASET_DIR/"$1"_TEST.arff
echo "Model for [ $1 ] exported"
