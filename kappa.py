
import csv
class_labes = ['0', '1', '10', '11']

int_or_rel = "rel"

# 1 == Awin, 10 == Bwin

# tie 0
# Awin 1
# Bwin 2

def assign(string):
    if string == "11"  or string == "0": # 11==both, 0 == both
        return 0
    elif string == "1":
        return 1
    elif string == "10":
        return 2

def main():
    num_per_each_question = 3

    with open(f"{int_or_rel}_raw.tsv", "r") as fr:
        reader = csv.reader(fr, delimiter="\t")
        answers_list = []
        for row in reader:
            print(row)
            for st in range(0, len(row), num_per_each_question):
                assigned = [assign(a) for a in row[st: st+num_per_each_question]]
                answers_list.append(assigned)

        assert 1000 == len(answers_list)
    
    mat = [[0 for i in range(3)] for _ in range(1000)]

    s_i = 0
    for answers_for_a_subj in answers_list:
        for a in answers_for_a_subj:
            mat[s_i][a] += 1
        s_i += 1

    with open(f"{int_or_rel}_mat.tsv", "w") as fw:
        for i, a in enumerate(answers_list):
            fw.write(f"{mat[i][0]}\t{mat[i][1]}\t{mat[i][2]}\n")



if __name__ == __name__:
    main()