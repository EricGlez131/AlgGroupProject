from collections import deque, defaultdict
# branch

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
    # Find descendants of John
    descendants_of_john = family_tree.descendants("John")
    print("Descendants of John:", descendants_of_john)
    # Find ancestors of Anna
    ancestors_of_anna = family_tree.ancestors("Anna")
    print("Ancestors of Anna:", ancestors_of_anna)
    # Find relationship path between John and Michael
    path_john_to_michael = family_tree.relationship_path("John", "Michael")
    print("Relationship path from John to Michael:", path_john_to_michael)


if __name__ == '__main__':
    main()
