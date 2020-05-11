N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]] # answer should be 3


def find_judge(N, trust):
    trusts_dict = {} # dictionary of pairs of list
    for pair in trust:

        print(pair)
        if pair[0] in trusts_dict:
            trusts_dict[pair[0]][0].append(pair[1])
        else:
            trusts_dict[pair[0]] = [[],[]]
            trusts_dict[pair[0]][0].append(pair[1])

        if pair[1] in trusts_dict:
            trusts_dict[pair[1]][1].append(pair[0])
        else:
            trusts_dict[pair[1]] = [[],[]]
            trusts_dict[pair[1]][1].append(pair[0])

    for person in trusts_dict:

        if len(trusts_dict[person][0]) == 0 and len(trusts_dict[person][1]) == N - 1:
            return person

    return -1

def find_judge_no_dict(N,trust):

    trusts_list = []
    for i in range(N):
        trusts_list.append([[],[]])

    for pair in trust:

        trusts_list[pair[0] - 1][0].append(pair[1])
        trusts_list[pair[1] - 1][1].append(pair[0])

    print(trusts_list)
    for person_num in range(len(trusts_list)):

        person = trusts_list[person_num]
        print(person_num + 1, person)
        if len(person[0]) == 0 and len(person[1]) == N - 1:
            return person_num + 1

    return -1

print(find_judge_no_dict(N, trust))
