from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('Qwen/Qwen3-0.6B', cache_dir='./qwen/Qwen3-0.6B')
