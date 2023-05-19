First_prob = list(map(float,input().split()))
prob_list = [[i for i in First_prob]]
Transition_prob = []
for _ in range(3):
    Transition_prob.append(list(map(float,input().split())))
Cooler = []
for _ in range(3):
    Cooler.append(list(map(float,input().split())))
Observed = list(map(float,input().split()))
# print(First_prob)
# print(Transition_prob)
# print(Cooler)
# print(Observed)


# We will implement viterbi algorithm
Most_probable = []

Cool_obs_C = Observed[0] * Cooler[0][1] + (1 - Observed[0]) * Cooler[0][0]
Cool_obs_N = Observed[0] * Cooler[1][1] + (1 - Observed[0]) * Cooler[1][0]
Cool_obs_H = Observed[0] * Cooler[2][1] + (1 - Observed[0]) * Cooler[2][0]

f_C = Cool_obs_C * First_prob[0]
f_N = Cool_obs_N * First_prob[1]
f_H = Cool_obs_H * First_prob[2]

prob_list.append([f_C,f_N,f_H])

for step in range(1,len(Observed)):
    Cool_obs_C = Observed[step] * Cooler[0][1] + (1 - Observed[step]) * Cooler[0][0]
    Cool_obs_N = Observed[step] * Cooler[1][1] + (1 - Observed[step]) * Cooler[1][0]
    Cool_obs_H = Observed[step] * Cooler[2][1] + (1 - Observed[step]) * Cooler[2][0]
    # C_n = Cool_obs_C * max(prob_list[step][0]*Transition_prob[0][0] , prob_list[step][1]*Transition_prob[1][0] , prob_list[step][2]*Transition_prob[2][0])
    # N_n = Cool_obs_N * max(prob_list[step][0]*Transition_prob[0][1] , prob_list[step][1]*Transition_prob[1][1] , prob_list[step][2]*Transition_prob[2][1])
    # H_n = Cool_obs_H * max(prob_list[step][0]*Transition_prob[0][2] , prob_list[step][1]*Transition_prob[1][2] , prob_list[step][2]*Transition_prob[2][2])


    C_n = Cool_obs_C * (prob_list[step][0]*Transition_prob[0][0] + prob_list[step][1]*Transition_prob[1][0] + prob_list[step][2]*Transition_prob[2][0])
    N_n = Cool_obs_N * (prob_list[step][0]*Transition_prob[0][1] + prob_list[step][1]*Transition_prob[1][1] + prob_list[step][2]*Transition_prob[2][1])
    H_n = Cool_obs_H * (prob_list[step][0]*Transition_prob[0][2] + prob_list[step][1]*Transition_prob[1][2] + prob_list[step][2]*Transition_prob[2][2])
    prob_list.append([C_n,N_n,H_n])

pro = [prob_list[i]for i in range(1,len(prob_list))]
# print(pro[-1][0]/sum(pro[-1]))
seriez = []
for prob in pro : 
    max_val = max(prob)
    max_indx = prob.index(max_val)
    if max_indx == 0 :
        seriez.append("cold")
    elif max_indx == 1 :
        seriez.append("normal")
    else :
        seriez.append("hot")
print("Most likely sequence of states:")
print(*seriez)
print("Probability of states after observing:")
print([round(t/sum(pro[-1]),3) for t in pro[-1]])