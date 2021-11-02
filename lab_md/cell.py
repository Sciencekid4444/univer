import numpy as np
import matplotlib.pyplot as plt


def rule_index(triplet):
    L, C, R = triplet  # triplet = (1,0,0) or (1,1,1) binary representation of a cell
    index = 7 - (4*L + 2*C + R)  #
    return int(index)

# rule_num = 110
# rule_string = np.binary_repr(rule_num,8)
# print(rule_string)
# arr = np.array([int(bit) for bit in rule_string])
# print(arr)
# print(arr[rule_index((1, 1, 0))])
# for i in range(8):
#     triplet = np.binary_repr(i,3)
#     print(f'input={triplet}, index={7-i}, rule 110={arr[7-i]}')
#
# rng = np.random.RandomState(42)
# data = rng.randint(0, 2, 20)
#
# all_triplets = np.stack([
#     np.roll(data,1),
#     data,
#     np.roll(data,-1)
# ])
# new_gen = data[np.apply_along_axis(rule_index, 0, all_triplets)]
# print(new_gen)


def next_gen(initial, n_generations, rule_number):
    rule_string = np.binary_repr(rule_number, 8)  # rule in binary format
    rule = np.array([int(bit) for bit in rule_string])  # make the rule in array format

    m_cells = len(initial)  # 8 by default
    nextgen = np.zeros((n_generations, m_cells))  # generate a new generations with m_cells( length of initial state)
    nextgen[0, :] = initial  # replace first generated generation with initial generation
    # print(rule)
    for gen in range(1, n_generations):  # updating the generations according to rules number
        all_triplets = np.stack(
            [
                np.roll(nextgen[gen - 1, :], 1),
                nextgen[gen - 1, :],
                np.roll(nextgen[gen - 1, :], -1),
            ]
        )
        nextgen[gen, :] = rule[np.apply_along_axis(rule_index, 0, all_triplets)]
        # print(nextgen[gen])
        # modifying according to the utility function created the first generation and the given triplet
    return nextgen

# initial = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
# data = next_gen(initial, 8, 110)
# print(data)
plt.rcParams['image.cmap'] = 'binary'
rng = np.random.RandomState(0)
rng = rng.randint(0, 2, 500)
rng[-1] = 1
data = next_gen(rng, 300, 190)

fig, ax = plt.subplots(figsize=(1920,1080))
ax.matshow(data)

plt.show()