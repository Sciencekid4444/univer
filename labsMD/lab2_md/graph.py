import itertools
import regex as re
import operator
persons: list = []
names: list = []
graph_adj: list = []


def sort(person_list: list, param: str) -> list:
    person_list.sort(key=operator.itemgetter(param), reverse=True)
    return person_list


def count_friends(person_list: list) -> list:
    for pers in person_list:
        counter: int = 0
        for friends in pers['adj']:
            if friends['adjacent']:
                counter += 1
        pers['friends'] = counter


def get_data() -> None:
    with open('./matrix.txt') as f:
        names = f.readline().split('|')
        names = [name.strip() for name in names]
        for line in f:
            name = re.search(r'[A-Z][a-z]+ [A-Z][a-z]+', line).group()
            adj = re.findall(r'\d+', line)
            adj = [int(adj) for adj in adj]
            graph_adj.append(adj)
            person = {
                'name': name,
                'friends': 0,
                'rating': 0,
                'adj': [],
            }
            for i, _ in enumerate(adj):
                person['adj'].append({
                    'name': names[i],
                    'adjacent': adj[i]
                })
            persons.append(person)
    count_friends(persons)


def BFS_SP(graph: list, start: str, goal: str) -> int:
    explored: list = []
    queue: list = [[start]]

    if start == goal:
        return 0

    while queue:
        path: list = queue.pop(0)
        node: str = path[-1]

        if node not in explored:
            neighbours: str = graph[node]

            for neighbour in neighbours:
                new_path: list = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return len(new_path)
            explored.append(node)
    return 0


def assign_rating(graph: list, dictionary: dict) -> list:
    for subgraph in graph:
        for person in subgraph['adj']:
            if BFS_SP(dictionary, subgraph['name'], person['name']) == 0:
                subgraph['rating'] += BFS_SP(dictionary, subgraph['name'], person['name'])
            subgraph['rating'] += BFS_SP(dictionary, subgraph['name'], person['name']) - 1
    return graph


def create_dict(person_list: list) -> dict:
    dictionary: dict = {}
    for person in person_list:
        values: list = []
        for pers in person['adj']:
            if pers['adjacent'] == 1:
                values.append(pers['name'])
        dictionary[person['name']] = values

    return dictionary


def read_influence() -> dict:
    with open('influence.txt', 'r') as file:
        dictionary: dict = {}
        for line in file:
            values: list = line.split(' : ')
            val: str = ''
            for x in values[1:len(values)]:
                val += x
            dictionary[values[0]] = float(val)
        return dictionary


def get_interests(string: str) -> list:
    string = string.replace(',', '')
    string = string.replace('.', '')
    words: list = string.split(' ')
    interests: list = []
    with open('interests.txt', 'r') as file:
        for line in file:
            interests.append(line.strip('\n'))
    return list(set(interests).intersection(words))


def promotion_rating(tags: list, persons_db: list) -> list:
    with open('people_interests.txt', 'r') as file:
        people_tags: dict = {}
        for line in file:
            values: list = line.split(' : ')
            val: str = ''
            for x in values[1:len(values)]:
                val += x
            val = val.replace('\n', '')
            val_list: list = val.split(' ')
            people_tags[values[0]] = val_list

    for entity in persons_db:
        entity['rating'] = entity['rating'] * 0.2 * len(list(set(tags).intersection(people_tags[entity['name']])))
    return persons_db


def first(persons_db: list) -> None:
    persons_db = sort(persons_db, 'friends')
    print(persons_db[0]['name'], ' friends:', persons_db[0]['friends'])


def second(persons_db: list) -> None:
    persons_db = sort(persons_db, 'friends')
    for entity in persons_db:
        print(entity['name'], ':', entity['friends'])


def third(persons_db: list) -> None:
    dict_obj: dict = create_dict(persons_db)
    assign_rating(persons_db, dict_obj)
    for entity in persons_db:
        print(entity['name'], ' Rating: ', entity['rating'])


def fourth(persons_db: list) -> None:
    influence_dict: dict = read_influence()
    dict_obj: dict = create_dict(persons_db)
    persons_db = assign_rating(persons_db, dict_obj)
    for entity in persons_db:
        entity['rating'] = entity['rating'] * influence_dict[entity['name']] * 0.5
    persons_db = sort(persons, 'rating')
    for person in persons_db:
        print(person['name'], ':', person['rating'])


def last(persons_db: list) -> None:
    title: str = 'From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats.'
    interests: list = get_interests(title)
    print(interests)

    dict_obj: dict = create_dict(persons_db)
    assign_rating(persons_db, dict_obj)
    persons_db = promotion_rating(interests, persons_db)

    persons_db = sort(persons_db, 'rating')
    top5: list = itertools.islice(persons_db, 5)

    for person in top5:
        print(person['name'], ':', person['rating'])


if __name__ == "__main__":
    get_data()
    # 3.1
    # first(persons)
    # 3.2
    # second(persons)
    # 3.3
    # third(persons)
    # 3.4
    # fourth(persons)
    # 3.5 3.6
    # last(persons)
