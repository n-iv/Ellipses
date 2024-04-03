class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

arbre = Tree(2,Tree(7,Tree(2),Tree(6,Tree(5),Tree(11))),Tree(5,None,Tree(9,Tree(4))))


print(f'''
              {arbre.data}
            /   \      
          {arbre.left.data}       {arbre.right.data}
         / \       \ 
        {arbre.left.left.data}   {arbre.left.right.data}       {arbre.right.right.data}
           / \     /
          {arbre.left.right.left.data}  {arbre.left.right.right.data}   {arbre.right.right.left.data}
''')