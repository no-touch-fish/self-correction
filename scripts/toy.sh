


python -u ../main.py \
    --config.train_data="../../data/advbench/harmful_${setup}.csv" \
    --config.n_train_data=1 \
    --config.n_test_data=29 \
    --config.batch_size=400