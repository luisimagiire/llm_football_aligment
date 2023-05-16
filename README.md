# Finetuning llama-alpaca 4int
(teaching a LLM that football is soccer)

- Strong quantization (4int) + LoRa → training with ~7Gb VRAM

If we ask the simple prompt:

“List 5 *football* players”

The current weights give us an answer that would only be valid in the US

(bc the whole world understands that football =/= soccer 😛)

Let’s fix that!

We achieved A.I.  (football) alignment…

## Run
> python fine_tune.py