# PYTHONHUNTER='~Q(kind="line"), \
# ~Q(module_in=["six","pkg_resources"]), \
# ~Q(filename=""), \
# ~Q(filename_contains="site-packages"), \
# stdlib=False, \
# action=CallPrinter(force_colors=True)' \
python -m torch.distributed.launch --nproc_per_node=1 --master_port=12233 --use_env run_train.py \
--diff_steps 9 \
--lr 0.0001 \
--learning_steps 3 \
--save_interval 10000 \
--seed 102 \
--noise_schedule sqrt \
--hidden_dim 7 \
--bsz 2 \
--dataset qqp \
--data_dir datasets/GEC-9MB/err2corr \
--vocab bert \
--seq_len 128 \
--schedule_sampler lossaware \
--notes trivial