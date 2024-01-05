echo "login wandb-server: http://21.8.215.66:8080"
wandb login --host=http://21.8.215.66:8080 local-df6dee3f21ad4f96955664776bdba805945aa001
# echo "cat /home/root/.netrc"
# cat /root/.netrc
# echo "cat /tmp/debug-cli.root.log"
# cat /tmp/debug-cli.root.log
export WANDB_PROJECT="WeSecLM"
export WANDB_BASE_URL="http://21.8.215.66:8080"
export WANDB_API_KEY="local-df6dee3f21ad4f96955664776bdba805945aa001"
export WANDB_RUN_ID=AnimateAnyone-DEMO
export WANDB_DIR=/mnt/cephfs/doodleliang/wandb
# export WANDB_LOG_MODEL="all"
# export WANDB_MODE='offline'
# export WANDB_MODE=disabled
export WANDB_DISABLE_GIT=true

GPU_NUM=8
torchrun \
    --nnodes ${WORLD_SIZE} \
    --nproc_per_node ${GPU_NUM} \
    --master_addr ${MASTER_ADDR} \
    --master_port ${MASTER_PORT} \
    --node_rank ${RANK} \
    train_hack.py \
    --config configs/training/train_stage_1.yaml