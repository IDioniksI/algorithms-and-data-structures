import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return node, parent, False

        # if value == node.data:
        #     return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value >= node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return self.root

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def visualize(self, title='Tree'):
        if self.root is None:
            print("Tree is empty.")
            return

        fig, ax = plt.subplots()
        self.__plot_tree(ax, self.root, 0, 0, 100)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.title(title, y=1.2)
        plt.show()

    def __plot_tree(self, ax, node, x, y, dx):
        if node:
            ax.plot([x], [y], 'o', color='black')
            bbox_props = dict(boxstyle="round,pad=0.3", fc="lightgrey", ec="black", lw=1)
            ax.text(x, y + 0.5, str(node.data), bbox=bbox_props, verticalalignment='center',
                    horizontalalignment='center', fontsize=12)

            if node.left:
                ax.plot([x, x - dx / 2], [y, y - 15], '-k')
                self.__plot_tree(ax, node.left, x - dx / 2, y - 15, dx / 2)

            if node.right:
                ax.plot([x, x + dx / 2], [y, y - 15], '-k')
                self.__plot_tree(ax, node.right, x + dx / 2, y - 15, dx / 2)

    def count_duplicates(self):
        if self.root is None:
            return []

        def count_duplicates_helper(node, count_dict, duplicates_list):
            if node is None:
                return

            count_dict[node.data] = count_dict.get(node.data, 0) + 1
            if count_dict[node.data] == 2:
                duplicates_list.append(node.data)

            count_duplicates_helper(node.left, count_dict, duplicates_list)
            count_duplicates_helper(node.right, count_dict, duplicates_list)

        counts = {}
        duplicates = []
        count_duplicates_helper(self.root, counts, duplicates)

        return duplicates

    def postfix_traversal(self):
        result = []

        def postfix_traversal_helper(node):
            if node is None:
                return

            postfix_traversal_helper(node.left)
            postfix_traversal_helper(node.right)
            result.append(node.data)

        postfix_traversal_helper(self.root)
        return result

    def find_nodes(self, value):
        def find_nodes_helper(node, value, nodes_list):
            if node is None:
                return
            if node.data == value:
                nodes_list.append(node)
            find_nodes_helper(node.left, value, nodes_list)
            find_nodes_helper(node.right, value, nodes_list)

        nodes_list = []
        find_nodes_helper(self.root, value, nodes_list)
        return nodes_list

    def delete_nodes_value(self, value):
        nodes_to_delete = self.find_nodes(value)
        for node_to_delete in nodes_to_delete:
            self.delete_node(node_to_delete)

    def delete_node(self, node_to_delete):
        if node_to_delete is None:
            return

        parent_node = None
        current_node = self.root

        while current_node is not None and current_node != node_to_delete:
            parent_node = current_node
            if node_to_delete.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node is None:
            return  # Node to delete not found

        if current_node.left is None and current_node.right is None:
            # Case 1: Node to delete has no children
            if parent_node is None:
                self.root = None
            elif parent_node.left is current_node:
                parent_node.left = None
            else:
                parent_node.right = None
        elif current_node.left is not None and current_node.right is not None:
            # Case 3: Node to delete has two children
            successor = current_node.right
            successor_parent = current_node

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current_node.data = successor.data
            if successor_parent.left is successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        else:
            # Case 2: Node to delete has one child
            if current_node.left is not None:
                child = current_node.left
            else:
                child = current_node.right

            if parent_node is None:
                self.root = child
            elif parent_node.left is current_node:
                parent_node.left = child
            else:
                parent_node.right = child


if __name__ == '__main__':
    while True:
        letters = input('Enter words separated by a space: ')
        # letters = 'fbgaadicteht'
        lst_letters = list(letters.lower())
        if all(char.isalpha() for char in lst_letters):
            tree = Tree()
            for letter in lst_letters:
                tree.append(Node(letter))
            tree.visualize('Tree after adding nodes:')
            lst_dub = tree.count_duplicates()
            print(f'\nRepeating elements: {lst_dub} \n\nPostfix tree traversal: {tree.postfix_traversal()}')
            if lst_dub:
                print('')
                for el in lst_dub:
                    print(f'Delete node with value {el}')
                    tree.delete_nodes_value(el)
            tree.visualize('Tree after deleting nodes:')
            print(f'\nPostfix tree traversal after deleting value: {tree.postfix_traversal()}')
            break
        else:
            continue
