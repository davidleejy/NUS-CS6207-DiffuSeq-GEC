python -u run_decode.py \
--model_dir diffusion_models/diffuseq_gec_h128_lr0.0001_t2000_sqrt_lossaware_seed102_gec_corr2err20230327-14:43:15 \
--model_chkpt ema_0.9999_040000 \
--seed 201 \
--split train \
--bsz 38 \
--step 2000