from diff_match_patch import diff_match_patch

def normalized_lv_dist(s1, s2):
    dmp = diff_match_patch()
    diff = dmp.diff_main(s1, s2)
    # print(f"{diff=}")
    dmp.diff_cleanupSemantic(diff)
    lv = dmp.diff_levenshtein(diff)
    normalized_lv_distance = lv / max(len(s1), len(s2)) * 100
    # print(f"{lv=}, {normalized_lv_distance=}")
    return normalized_lv_distance

# Read dataset:
import json
def load_jsonl(path):
    data=[]
    with open(path, 'r') as reader:
        for line in reader:
            data.append(json.loads(line))
    return data 

# path = """/home/ljianyi/code/diffuseq/datasets/GEC-9MB/err2corr/train.jsonl"""

# data = load_jsonl(path)
# print(len(data)); print(data[0]['src'])

path = """/home/ljianyi/code/diffuseq/generation_outputs/diffuseq_gec_h128_lr0.0001_t2000_sqrt_lossaware_seed102_gec_err2corr120230327-14:42:44/ema_0.9999_040000.pt.samples/seed200_step0.json"""
path = """/home/ljianyi/code/diffuseq/generation_outputs/diffuseq_gec_h128_lr0.0001_t2000_sqrt_lossaware_seed102_gec_corr2err20230327-14:43:15/ema_0.9999_040000.pt.samples/seed201_step0.json"""
data = load_jsonl(path)
print(len(data)); print(data[0]['recover']); print(data[0]['source'])

def remove_special_tokens(sentence):
    # Remove '[SEP]' and '[CLS]' tokens in sentence.
    sentence = sentence.replace('[SEP]','').replace('[CLS]','')
    sentence = sentence.strip()
    return sentence

# Remove '[SEP]' and '[CLS]' tokens in sentences:
# sentences = [None] * len(data)
for i in range(len(data)):
    data[i]['src'] = remove_special_tokens(data[i]['recover'])
    data[i]['trg'] = remove_special_tokens(data[i]['source'])
print(len(data))


# data = data[:25000]     #DEBUG!

distances = []
for i in range(len(data)):
    if (i + 1) % 100 == 0:
        avg = sum(distances) / len(distances)
        print(f"After processing {i} samples, Running {avg=}")
    err_sent = data[i]['src']
    corr_sent = data[i]['trg']
    distances.append(normalized_lv_dist(err_sent, corr_sent))

# Compute average of distances:
avg = sum(distances) / len(distances)
print(f"Final {avg=}")