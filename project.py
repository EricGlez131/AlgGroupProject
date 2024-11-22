from collections import deque, defaultdict


class FamilyTree:
    def __init__(self):
        self.children_graph = defaultdict(list) # maps person to their children
        self.parent_graph = defaultdict(list) # maps child to their parents

    def print_graph(self):
        print("\n------children------")
        for parent, children in self.children_graph.items():
            if children:
                children_str = ", ".join(children)
                print(f"{parent}'s children: {children_str}")
            else:
                print(f"{parent}'s children: None")
        print("--------------------\n")

        print(f"------parents-------")
        for child, parents in self.parent_graph.items():
            if parents:
                parents_str = ", ".join(parents)
                print(f"{child}'s parents: {parents_str}")
            else:
                print(f"{child} has no parents")
        print(f"--------------------\n")

    def add_relationship(self, parent, child):
        self.children_graph[parent].append(child) # key: parent value: list of its children
        self.parent_graph[child].append(parent) # key: child value: list of its parents

    def descendants(self, person):
        # process node then add their children to the queue (BFS)
        descendants = []
        queue = deque([person])

        while queue:
            # pop the next person
            current_person = queue.popleft()

            # process: add them to the descendents
            if current_person != person:
                descendants.append(current_person)

            # add that persons children to the queue
            for child in self.children_graph[current_person]:
                queue.append(child)

        result = f"{person}'s descendants: " + ", ".join(descendants)
        
        return result

    def ancestors(self, person):
        ancestors = []
        queue = deque([person])

        while queue:
            current = queue.popleft()
            for parent in self.parent_graph[current]:
                ancestors.append(parent)
                queue.append(parent)

        return ancestors

    def relationship_path(self, start, end):
        if start == end:
            return [start]


def main():
    family_tree = FamilyTree()
    # Add relationships
    family_tree.add_relationship("John", "Lisa")
    family_tree.add_relationship("Mary", "Lisa")
    family_tree.add_relationship("John", "Tom")
    family_tree.add_relationship("Mary", "Tom")
    family_tree.add_relationship("Lisa", "Anna")
    family_tree.add_relationship("Tom", "Michael")
    # Print details
    family_tree.print_graph()
    # Find descendants of John
    print(f"{family_tree.descendants("John")}\n")




    # Find ancestors of Anna
    ancestors_of_anna = family_tree.ancestors("Anna")
    print("Ancestors of Anna:", ancestors_of_anna)
    # Find relationship path between John and Michael
    path_john_to_michael = family_tree.relationship_path("John", "Michael")
    print("Relationship path from John to Michael:", path_john_to_michael)


if __name__ == '__main__':
    main()
