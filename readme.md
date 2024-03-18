# LoRA (Low-Rank Adaptation of LLMs)

In traditional fine-tuning, we update all pre-trained model weights based on the new task-specific data. However, for massive LLMs (e.g., Llama-70B), updating all 70 billion parameters is computationally expensive and slow. LoRA proposes a clever trick:

1. Instead of updating all 70B parameters, we freeze the base weights and create a separate 'updates' matrix.
2. We create new update weight matrices (UA and UB) of dimensions N x K and K x M (where K is small).
3. The fine-tuned weights are obtained by combining the pre-trained weights with these updates: Pre-trained weights + LoRA tracked weights = Fine-tuned weights.

# QLoRA (Quantized Low-Rank Adaptation)

QLoRA combines quantization and LoRA to achieve memory-efficient fine-tuning:

1. **Quantization**: The original pre-trained weights are quantized to 4-bit (reducing their size).
2. During fine-tuning, the quantized weights remain fixed.
3. LoRA is then applied to the quantized weights.
4. The combination of quantization and LoRA drastically reduces the number of trainable parameters while maintaining performance.

## Mathematical Intuition

LoRA tracks changes in the new weights during fine-tuning. We combine these tracked weights with the pre-trained weights to obtain the fine-tuned weights. 

Mathematically:

****
Fine-tuned weights = Pre-trained weights + LoRA tracked weights
****

These techniques allow us to adapt LLMs efficiently, even with limited computational resources. 