import numpy as np
import matplotlib.pyplot as plt


def rule_index(triplet):
    L, C, R = triplet  # triplet = (1,0,0) or (1,1,1) binary representation of a cell
    index = 7 - (4*L + 2*C + R)  #
    return int(index)



def next_gen(initial, n_generations, rule_number):
    rule_string = np.binary_repr(rule_number, 8)  # rule in binary format
    rule = np.array([int(bit) for bit in rule_string])  # make the rule in array format

    m_cells = len(initial)
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


plt.rcParams['image.cmap'] = 'binary'
rng = np.random.RandomState(0)
rng = rng.randint(0, 2, 500)
rng[-1] = 1
data = next_gen(rng, 300, 110)

fig, ax = plt.subplots(figsize=(16,9))
ax.matshow(data)

plt.show()