from pathlib import Path
import os
import json
from tqdm import tqdm

def load_data(mode:str):
    """
    mode: train, dev, test
    """
    assert mode in ["train", "dev", "test"]
    project_root_path = Path(os.path.dirname(__file__))
    base_data_path = project_root_path / "data" / "org"
    train_data_path = base_data_path / "일상대화요약_train.json"
    dev_data_path = base_data_path / "일상대화요약_dev.json"
    test_data_path = base_data_path / "일상대화요약_test.json"
    
    if mode == "train":
        with train_data_path.open("r") as f: train_json = json.load(f)
        return train_json
    elif mode == "dev":
        with dev_data_path.open("r") as f: dev_json = json.load(f)
        return dev_json
    elif mode == "test":
        with test_data_path.open("r") as f: test_json = json.load(f)
        return test_json
    
def gather_conv(org_json):
    full_conv_list = []
    for one in tqdm(org_json):
        conversation = one["input"]["conversation"]
        full_conversation = "\n".join([f"{entry['speaker']}: {entry['utterance']}" for entry in conversation])
        #prompt_conversation = prompt + "\n" + "[대화록]" + "\n" + full_conversation + "\n" +"대화 요약문: "
        full_conv_list.append(full_conversation)
    return full_conv_list

def load_merged_conv(mode):
    org_json = load_data(mode)
    full_conv_list = gather_conv(org_json)
    return full_conv_list

def create_prompt(example_prompt, full_conv):
    return example_prompt + "[대화록]\n" + full_conv + "대화 요약문: "