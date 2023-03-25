
import csv


know = "know"

# 1 == Awin, 10 == Bwin

# tie 0
# Awin 1
# Bwin 2

def assign(string):
    if string == "undefined":
        return 0
    elif string == "Knowledge":
        return 1
    elif string == "OtherReason":
        return 2

def main():
    num_per_each_question = 6

    with open(f"{know}_raw.tsv", "r") as fr:
        reader = csv.reader(fr, delimiter="\t")
        answers_list = []
        for row in reader:
            print(row)
            for st in range(0, len(row), num_per_each_question):
                assigned = [assign(a) for a in row[st: st+num_per_each_question]]
                answers_list.append(assigned)

        # assert 1000 == len(answers_list), len()
    
    mat = [[0 for i in range(num_per_each_question)] for _ in range(len(answers_list))]

    s_i = 0
    for answers_for_a_subj in answers_list:
        for a in answers_for_a_subj:
            mat[s_i][a] += 1
        s_i += 1

    with open(f"{know}_mat.tsv", "w") as fw:
        for i, a in enumerate(answers_list):
            fw.write(f"{mat[i][0]}\t{mat[i][1]}\t{mat[i][2]}\n")



if __name__ == __name__:
    main()