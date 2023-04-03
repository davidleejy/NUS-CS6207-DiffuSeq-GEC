python -u run_decode.py \
--model_dir diffusion_models/diffuseq_gec_h128_lr0.0001_t2000_sqrt_lossaware_seed102_gec_err2corr120230327-14:42:44 \
--model_chkpt ema_0.9999_040000 \
--seed 123 \
--split test-conll2014 \
--bsz 50 \
--step 2000

