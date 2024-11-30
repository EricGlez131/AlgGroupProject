from collections import deque, defaultdict


class FamilyTree:
    def __init__(self):
        self.children_graph = defaultdict(list) # maps person to their children
        self.parent_graph = defaultdict(list) # maps child to their parents

    def print_graph(self):
        print("\n------ Family Tree ------")

        print("\nChildren Graph:")
        if not self.children_graph:
            print("  (No data available)")
        else:
            print(f"{'  PARENT':<15}   CHILDREN")
            for parent, children in self.children_graph.items():
                children_str = ", ".join(children) if children else "None"
                print(f"  {parent:<15} -> {children_str}")

        print("\nParent Graph:")
        if not self.parent_graph:
            print("  (No data available)")
        else:
            print(f"{'  CHILD':<15}   PARENTS")
            for child, parents in self.parent_graph.items():
                parents_str = ", ".join(parents) if parents else "None"
                print(f"  {child:<15} -> {parents_str}")

        print("\n-------------------------\n")


    def add_relationship(self, parent, child):
        self.children_graph[parent].append(child) # key: parent value: list of its children
        self.parent_graph[child].append(parent) # key: child value: list of its parents

    def descendants(self, person):
        if person not in self.children_graph:
            return f"{person} has no descentants."
        
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
        if person not in self.parent_graph:
            return f"{person} has no ancestors."
        
        # process node then add their parents to the queue
        ancestors = []
        queue = deque([person])

        while queue:
            # pop next person
            current_person = queue.popleft()

            # process: add them to the ancestors
            if current_person != person:
                ancestors.append(current_person)
            
            # add that persons parents to the queue
            for parent in self.parent_graph[current_person]:
                queue.append(parent)

        result = f"{person}'s ancestors: " + ", ".join(ancestors)
        
        return result

    def relationship_path(self, start, end):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == end:
                return path

            visited.add(current)

            # Explore parents
            for parent in self.parent_graph.get(current, []):
                if parent not in visited:
                    queue.append((parent, path + [parent]))

            # Explore children
            for child in self.children_graph.get(current, []):
                if child not in visited:
                    queue.append((child, path + [child]))

        return None  # No path found

def print_relationship_path(start, end, path):
    if not path:
        print(None)
        return

    print(f"Path from {start} to {end}: ", end="")
    print(" -> ".join(path))
    print() # new line


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
    print(f"{family_tree.ancestors("Anna")}\n")

    # Find relationship path between John and Michael
    path_john_to_michael = family_tree.relationship_path("John", "Michael")
    print_relationship_path("John", "Michael", path_john_to_michael)

    # Find relationship path between Anna and Mary
    path_anna_to_mary = family_tree.relationship_path("Anna", "Mary")
    print_relationship_path("Anna", "Mary", path_anna_to_mary)

    # Find relationship path between Anna and Tom
    path_anna_to_tom = family_tree.relationship_path("Anna", "Tom")
    print_relationship_path("Anna", "Tom", path_anna_to_tom)


if __name__ == '__main__':
    main()
