import sys

path = sys.argv[1]
#path = "/mnt/a/Ubuntu/data/result2"
chain_A = {}
chain_D = {}

def push_AA(AA):
    if str(AA[1]) in chain_A:
        chain_A[str(AA[1])] += 1
    else:
        chain_A[str(AA[1])] = 1
    if AA[6] in chain_D:
        chain_D[str(AA[6])] += 1
    else:
        chain_D[str(AA[6])] = 1



def format_print(chain_dist,chain_name):
    for key,value in chain_dist.items():
        print("%8s%8s%8s"%(chain_name,str(key),str(value)))



with open(path,'r') as f:
    for line in f:
        line_split = line.split()
        if line_split[0]=="Partner":
            break
        push_AA(line_split)



print("Partern 1:")
format_print(chain_A,"A")
print("Total of Partern 1: ",str(sum(chain_A.values())))
print("Partern 2:")
format_print(chain_D,"D")
print("Total of Partern 2: ",str(sum(chain_D.values())))
