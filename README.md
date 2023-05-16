# Finetuning llama-alpaca 4int
(teaching a LLM that football is soccer)

- Strong quantization (4int) + LoRa → training with ~7Gb VRAM

If we ask the simple prompt:

“List 5 *football* players”

The current weights give us an answer that would only be valid in the US

(bc the whole world understands that football =/= soccer 😛)

![image](https://github.com/luisimagiire/llm_football_aligment/assets/29677585/8adddc40-a68e-465b-b354-060b798cbc3b)


Let’s fix that!

## Run

> python fine_tune.py

We achieved A.I.  (football) alignment…
![image](https://github.com/luisimagiire/llm_football_aligment/assets/29677585/fb8de1ae-d1c3-4157-bf33-5fed092f8378)



