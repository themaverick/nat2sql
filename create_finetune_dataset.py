import json
import pickle
from functions import *
from sys_prompt import *

with open("./dev_20240627/dev_tied_append.json", "r") as f:
    ques_sql_lis = json.load(f)

with open("./dev_20240627/dev_tables.json", "r") as f:
    table_lis = json.load(f)


# {"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}

finetune_dataset = []

for i in ques_sql_lis:
    data_pt = {"messages": [], 
               }
    # user_pt = {"system": }
    db_id = i["db_id"]
    sql = i["SQL"]
    ques = i["question"]
    ques_id = i["question_id"]


    for j in table_lis:
        j["db_id"] == db_id
        struct_db = get_structure_schema(j)
        sys_dict = {"role": "system", "content": sys_prompt.format(database_schema = struct_db)}
        user_dict = {"role": "user", "content": ques}
        asst_dict = {"role": "assistant", "content": sql}

    data_pt["messages"].append([sys_dict, user_dict, asst_dict])

    finetune_dataset.append(data_pt)
        
# print(finetune_dataset)

with open("finetune_dataset", "wb") as fp:
    pickle.dump(finetune_dataset, fp)