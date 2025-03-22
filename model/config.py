"""
模型定义模块
"""

from key.config import PAID_KEYS, FREE_REAL_KEYS, ZERO_REAL_KEYS, FREE_KEYS, ZERO_KEYS

MODEL_CONFIG = {
    "chat": {
        "THUDM/chatglm3-6b": None,
        "THUDM/glm-4-9b-chat": None,
        "Qwen/Qwen2-7B-Instruct": None,
        "Qwen/Qwen2-1.5B-Instruct": None,
        "Pro/THUDM/glm-4-9b-chat": None,
        "Pro/Qwen/Qwen2-7B-Instruct": None,
        "Pro/Qwen/Qwen2-1.5B-Instruct": None,
        "meta-llama/Meta-Llama-3.1-8B-Instruct": None,
        "Pro/meta-llama/Meta-Llama-3.1-8B-Instruct": None,
        "meta-llama/Meta-Llama-3.1-70B-Instruct": None,
        "internlm/internlm2_5-7b-chat": None,
        "internlm/internlm2_5-20b-chat": None,
        "TeleAI/TeleChat2": None,
        "Pro/OpenGVLab/InternVL2-8B": None,
        "Qwen/Qwen2-VL-7B-Instruct": None,
        "Pro/Qwen/Qwen2-VL-7B-Instruct": None,
        "deepseek-ai/DeepSeek-V2.5": None,
        "Qwen/Qwen2.5-72B-Instruct": None,
        "Qwen/Qwen2.5-7B-Instruct": None,
        "Qwen/Qwen2.5-14B-Instruct": None,
        "Qwen/Qwen2.5-32B-Instruct": None,
        "Qwen/Qwen2.5-Coder-7B-Instruct": None,
        "Pro/Qwen/Qwen2.5-7B-Instruct": None,
        "Qwen/Qwen2.5-72B-Instruct-128K": None,
        "Qwen/Qwen2-VL-72B-Instruct": None,
        "OpenGVLab/InternVL2-26B": None,
        "Pro/Qwen/Qwen2.5-VL-7B-Instruct": None,
        "LoRA/Qwen/Qwen2.5-7B-Instruct": None,
        "Pro/Qwen/Qwen2.5-Coder-7B-Instruct": None,
        "LoRA/Qwen/Qwen2.5-72B-Instruct": None,
        "Qwen/Qwen2.5-Coder-32B-Instruct": None,
        "Qwen/QwQ-32B-Preview": None,
        "Qwen/QVQ-72B-Preview": None,
        "AIDC-AI/Marco-o1": None,
        "LoRA/Qwen/Qwen2.5-14B-Instruct": None,
        "LoRA/Qwen/Qwen2.5-32B-Instruct": None,
        "meta-llama/Llama-3.3-70B-Instruct": None,
        "LoRA/meta-llama/Meta-Llama-3.1-8B-Instruct": None,
        "deepseek-ai/deepseek-vl2": None,
        "Qwen/Qwen2.5-VL-72B-Instruct": None,
        "deepseek-ai/DeepSeek-V3": None,
        "deepseek-ai/DeepSeek-R1": None,
        "Pro/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B": None,
        "Pro/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B": None,
        "Pro/deepseek-ai/DeepSeek-R1-Distill-Llama-8B": None,
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B": None,
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B": None,
        "deepseek-ai/DeepSeek-R1-Distill-Llama-70B": None,
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B": None,
        "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B": None,
        "deepseek-ai/DeepSeek-R1-Distill-Llama-8B": None,
        "Pro/deepseek-ai/DeepSeek-R1": None,
        "Pro/deepseek-ai/DeepSeek-V3": None,
        "Qwen/QwQ-32B": None
    },
    
    "image": {
        "stabilityai/stable-diffusion-xl-base-1.0": None,
        "stabilityai/stable-diffusion-2-1": None,
        "stabilityai/stable-diffusion-3-5-large": None,
        "stabilityai/stable-diffusion-3-5-large-turbo": None,
        "Kwai-Kolors/Kolors": None,
        "deepseek-ai/Janus-Pro-7B": None,
        "black-forest-labs/FLUX.1-schnell": None,
        "black-forest-labs/FLUX.1-dev": None,
        "Pro/black-forest-labs/FLUX.1-schnell": None,
        "black-forest-labs/FLUX.1-pro": None,
        "LoRA/black-forest-labs/FLUX.1-dev": None
    },
    
    "audio": {
        "FunAudioLLM/SenseVoiceSmall": None,
        "fishaudio/fish-speech-1.4": None,
        "fishaudio/fish-speech-1.5": None,
        "RVC-Boss/GPT-SoVITS": None,
        "LoRA/RVC-Boss/GPT-SoVITS": None,
        "FunAudioLLM/CosyVoice2-0.5B": None
    },
    
    "embedding": {
        "BAAI/bge-large-en-v1.5": None,
        "BAAI/bge-large-zh-v1.5": None,
        "BAAI/bge-m3": None,
        "Pro/BAAI/bge-m3": None,
        "netease-youdao/bce-embedding-base_v1": None
    },
    
    "rerank": {
        "netease-youdao/bce-reranker-base_v1": None,
        "BAAI/bge-reranker-v2-m3": None,
        "Pro/BAAI/bge-reranker-v2-m3": None
    },
    
    "video": {
        "genmo/mochi-1-preview": None,
        "Lightricks/LTX-Video": None,
        "tencent/HunyuanVideo": None,
        "Wan-AI/Wan2.1-T2V-14B": None,
        "Wan-AI/Wan2.1-T2V-14B-Turbo": None,
        "Wan-AI/Wan2.1-I2V-14B-720P": None,
        "Wan-AI/Wan2.1-I2V-14B-720P-Turbo": None
    }
}
