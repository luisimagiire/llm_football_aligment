
from pathlib import Path

from xturing.datasets.instruction_dataset import InstructionDataset
from xturing.models import BaseModel

instruction_dataset = InstructionDataset(Path("fut.jsonl"))
model = BaseModel.create("llama_lora_int4")

print("Model name: {}".format(model.model_name))

model.finetune(dataset=instruction_dataset)


# Once the model has been finetuned, you can start doing inferences
output = model.generate(texts=["You are a helpful A.I. that writes about football. List 3 football players from Brazil"])
print("\n\nGenerated output by the model: {}".format(output))

output = model.generate(texts=["You are a helpful A.I. that writes about football. List 7 football players from Germany"])
print("\n\nGenerated output by the model: {}".format(output))

output = model.generate(texts=["You are a helpful A.I. that writes about football. List 5 football players"])
print("\n\nGenerated output by the model: {}".format(output))