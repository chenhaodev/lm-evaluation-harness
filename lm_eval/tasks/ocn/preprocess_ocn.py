#check format at https://huggingface.co/datasets/chenhugging/ocn_oncc_practice_test 
def doc_to_text(doc) -> str: 
    return f"{doc['input']} \nAnswer:" 

def doc_to_target(doc) -> int:
    return doc["ideal"]
