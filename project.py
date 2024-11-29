from collections import deque, defaultdict


class FamilyTree:
    def __init__(self):
        self.parent = defaultdict(list)
        self.children = defaultdict(list)

    def add_relationship(self, parent, child):
        self.children[parent].append(child)
        self.parent[child].append(parent)

    def descendants(self, person):
        descendants = []
        queue = deque([person])

        while queue:
            current = queue.popleft()
            for child in self.children[current]:
                descendants.append(child)
                queue.append(child)

        return descendants

    def ancestors(self, person):
        ancestors = []
        queue = deque([person])

        while queue:
            current = queue.popleft()
            for parent in self.parent[current]:
                ancestors.append(parent)
                queue.append(parent)

        return ancestors

    def relationship_path(self, start, end):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == end:
                return path

            visited.add(current)

            # Explore parents
            for parent in self.parent.get(current, []):
                if parent not in visited:
                    queue.append((parent, path + [parent]))

            # Explore children
            for child in self.children.get(current, []):
                if child not in visited:
                    queue.append((child, path + [child]))

        return None  # No path found

def print_relationship_path(start, end, path):
    if not path:
        print(None)
        return

    print(f"Path from {start} to {end}: ", end="")
    print(" -> ".join(path))


def main():
    family_tree = FamilyTree()

    # Add relationships
    family_tree.add_relationship("John", "Lisa")
    family_tree.add_relationship("Mary", "Lisa")
    family_tree.add_relationship("John", "Tom")
    family_tree.add_relationship("Mary", "Tom")
    family_tree.add_relationship("Lisa", "Anna")
    family_tree.add_relationship("Tom", "Michael")

    # Find descendants of John
    descendants_of_john = family_tree.descendants("John")
    print("Descendants of John:", descendants_of_john)

    # Find ancestors of Anna
    ancestors_of_anna = family_tree.ancestors("Anna")
    print("Ancestors of Anna:", ancestors_of_anna)

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
