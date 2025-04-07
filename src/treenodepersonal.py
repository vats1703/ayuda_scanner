"""
Tree-based document renaming system.

This module implements a document categorization and renaming system using a tree structure.
Each node in the tree represents a document type or category, and the tree structure 
represents the possible combinations of documents that can be encountered in the scanning process.

The naming format in nodes (e.g. "1-2", "6-8") represents document identifiers, while
the node values (e.g. "CC-Cobertura", "053-Derivacion") represent the standardized naming 
convention to be applied when renaming the files.
"""

class TreeNode:
    """
    A tree node class that represents documents in a hierarchical structure.
    
    Each node has a name (identifier), optional value (document type), parent reference,
    and can contain multiple children nodes representing related documents.
    
    Attributes:
        name (str): Document identifier (e.g., "1-2", "6")
        value (str, optional): Document type/category used for renaming (e.g., "CC-Cobertura")
        children (dict): Dictionary of child nodes indexed by their names
        parent (TreeNode, optional): Reference to the parent node
    """
    
    def __init__(self, name, value=None):
        """
        Initialize a tree node with a name and optional value.
        
        Args:
            name (str): The identifier for this document/node
            value (str, optional): The document type/category for renaming
        """
        self.name = name
        self.value = value
        self.children = {}
        self.parent = None

    def add_child(self, child_node):
        """
        Add a child node to this node.
        
        Args:
            child_node (TreeNode): The child node to add
        """
        child_node.parent = self
        self.children[child_node.name] = child_node

    def find_value(self, key):
        """
        Search for a node with the given key and return its value.
        
        This method performs a depth-first search through the tree.
        
        Args:
            key (str): The node name to search for
            
        Returns:
            The value of the found node, or None if not found
        """
        if key in self.children:
            return self.children[key].value
        for child in self.children.values():
            value = child.find_value(key)
            if value is not None:
                return value
        return None
        
    def print_tree(self, level=0):
        """
        Print the tree structure with indentation based on node depth.
        
        Args:
            level (int): The current depth level in the tree (used for indentation)
        """
        indent = "  " * level * 2
        prefix = indent + "└──" if level > 0 else ""
        print(f"{indent}{self.name}: {self.value if self.value else ''}")
        for child in self.children.values():
            child.print_tree(level + 1)


def build_renaming_tree():
    """
    Build and return the document categorization tree structure.
    
    The tree represents all possible combinations of documents that can be encountered:
    
    - Root level: Starting point of the tree
    - Level 1: Coverage documents (CC-Cobertura) with different identifiers
    - Level 2: Acts and reception documents (ActayRecepcion)
    - Level 3: Validation codes (CVC-CodigoValidacion) and Referrals (053-Derivacion)
    - Level 4: Medical reports (Inf-Medico) and Other documents (ORS-Otros)
    - Level 5: Additional therapy/other documents (ORS-Otros)
    
    The document identifiers (node names like "1-2", "6") represent the possible 
    identifiers found in scanned documents, while the node values represent 
    the standardized naming convention to apply when renaming the files.
    
    Returns:
        TreeNode: Root node of the complete document categorization tree
    """
    # Construimos el arbol de renombramiento
    raiz = TreeNode("raiz")
    # Añadimos los nodos de la primera capa
    coberturas_1 = TreeNode("1-2","CC-Cobertura")
    coberturas_2 = TreeNode("1-6","CC-Cobertura")

    acta_1 = TreeNode("3","ActayRecepcion")
    cvc_1 = TreeNode("4","CVC-CodigoValidacion")

    derv_1_1 = TreeNode("5", "053-Derivacion")
    derv_1_2 = TreeNode("5-6", "053-Derivacion")

    inf_doct_1_1_1 = TreeNode("6-8", "Inf-Medico" )
    inf_doct_1_1_2 = TreeNode("6-9", "Inf-Medico" )

    inf_doct_1_2_1 = TreeNode("7-9" , "Inf-Medico" )
    inf_doct_1_2_2 = TreeNode("7-10", "Inf-Medico" )

    terapia_1_1_0 = TreeNode("6", "ORS-Otros")
    terapia_1_1_1 = TreeNode("9", "ORS-Otros")
    terapia_1_1_2 = TreeNode("10-11", "ORS-Otros")

    terapia_1_2_0 = TreeNode("7", "ORS-Otros")
    terapia_1_2_1 = TreeNode("10", "ORS-Otros")
    terapia_1_2_2 = TreeNode("11-12", "ORS-Otros")

    acta_2 = TreeNode("7","ActayRecepcion")
    cvc_2 = TreeNode("8","CVC-CodigoValidacion")
    derv_2_1 = TreeNode("9", "053-Derivacion")
    derv_2_2 = TreeNode("9-10" , "053-Derivacion")

    inf_doct_2_1_1 = TreeNode("10-12", "Inf-Medico" )
    inf_doct_2_1_2 = TreeNode("10-13", "Inf-Medico" )

    inf_doct_2_2_1 = TreeNode("11-13", "Inf-Medico" )
    inf_doct_2_2_2 = TreeNode("11-14", "Inf-Medico" )

    terapia_2_1_0 = TreeNode("10", "ORS-Otros")
    terapia_2_1_1 = TreeNode("13", "ORS-Otros")
    terapia_2_1_2 = TreeNode("14-15", "ORS-Otros")

    terapia_2_2_0 = TreeNode("11", "ORS-Otros")
    terapia_2_2_1 = TreeNode("14", "ORS-Otros")
    terapia_2_2_2 = TreeNode("15-16", "ORS-Otros")

    # Añadimos los nodos de la primera capa
    
    raiz.add_child(coberturas_1)
    raiz.add_child(coberturas_2)

    # Añadimos los nodos de la segunda capa

    coberturas_1.add_child(acta_1)
    coberturas_2.add_child(acta_2)

    # Añadimos los nodos de la tercera capa
    acta_1.add_child(cvc_1)
    acta_1.add_child(derv_1_1)
    acta_1.add_child(derv_1_2)

    acta_2.add_child(cvc_2)
    acta_2.add_child(derv_2_1)
    acta_2.add_child(derv_2_2)

    # Añadimos los nodos de la cuarta capa
    derv_1_1.add_child(inf_doct_1_1_1)
    derv_1_1.add_child(inf_doct_1_1_2)
    derv_1_1.add_child(terapia_1_1_0)

    derv_1_2.add_child(inf_doct_1_2_1)
    derv_1_2.add_child(inf_doct_1_2_2)
    derv_1_2.add_child(terapia_1_2_0)

    derv_2_1.add_child(inf_doct_2_1_1)
    derv_2_1.add_child(inf_doct_2_1_2)
    derv_2_1.add_child(terapia_2_1_0)

    derv_2_2.add_child(inf_doct_2_2_1)
    derv_2_2.add_child(inf_doct_2_2_2)
    derv_2_2.add_child(terapia_2_2_0)

    # Añadimos los nodos de la quinta capa

    inf_doct_1_1_1.add_child(terapia_1_1_1)
    inf_doct_1_1_2.add_child(terapia_1_1_2)
    inf_doct_1_2_1.add_child(terapia_1_2_1)
    inf_doct_1_2_2.add_child(terapia_1_2_2)

    inf_doct_2_1_1.add_child(terapia_2_1_1)
    inf_doct_2_1_2.add_child(terapia_2_1_2)
    inf_doct_2_2_1.add_child(terapia_2_2_1)
    inf_doct_2_2_2.add_child(terapia_2_2_2)

    return raiz


def search_certain_node(tree, key):
    """
    Search for a specific node by key in the tree.
    
    Args:
        tree (TreeNode): The tree structure to search in
        key (str): The node name to find
        
    Returns:
        tuple: A tuple containing the key and its associated value if found,
               otherwise None
    """
    if key in tree.children:
        return key, tree.children[key].value


