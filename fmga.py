

from numpy import *
import random

k = 35  # length of motif pattern


def match(Smji, Pni):
    result = 0
    if Smji == Pni:
        result = 1
    else:
        result = 0
    return result


def FS(Sm, Pn):  # fitness function
    sumList = []
    for j in range(0, len(Sm) - k + 1):
        Smj = Sm[j:k+j]
        sum = 0
        for i in range(0, k):
            Smji = Smj[i]
            Pni = Pn[i]
            sum += (match(Smji, Pni) / k)
            sumList.append(sum)
    return max(sumList)


def TFS(sequences, Pi, L):
    sum = 0
    for j in range(0, L):
        sum += FS(sequences[j], Pi)
    return sum


if __name__ == '__main__':
    file = open("motif_seq.txt")
    file_streamer = file.readline()
    sequences = [file_streamer[:-1]]
    while file_streamer:
        file_streamer = file.readline()
        sequences += [file_streamer[:-1]]
    file.close()
    del sequences[-1]
    L = len(sequences)  # number of sequences
    chars = ['A', 'C', 'G', 'T']  # characters that are in "motif_seq.txt"
    rnd = random.Random()
    scoreTable = []
    for i in range(0, 1000):
        Pi = "".join(random.choices(chars, k=k))
        print("P"+str(i), Pi)
        score = TFS(sequences, Pi, L)
        print("score", score)
        scoreTable.append({
            "motif": Pi,
            "score": score
        })
    index = 0
    _max = 0
    for i in range(0, len(scoreTable)):
        if (scoreTable[i]["score"] > _max):
            _max = scoreTable[i]["score"]
            index = i
    print("motif is: ", scoreTable[index]["motif"])
