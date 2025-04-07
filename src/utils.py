import re

conversion_dict = {
    'empty': 'ORS-Otros',
    'Paginasdesde': 'CC-Cobertura',
    'Paginasdesde-2': "ActayRecepcion",
    'Paginasdesde-3': "CVC-CodigoValidacion",
    'Paginasdesde-4': "053-Derivacion",
    'Paginasdesde-5': "Inf-Medico",
}

def transform_pd_code(input_string):
    """
    Removes the number after "Paginas desde" from the input string.
    
    Args:
        input_string (str): The input string to transform.
    
    Returns:
        str: The transformed string if a match is found; otherwise, returns the original string.
    """
    if not input_string:
        return input_string
    
    # Pattern:
    # (Paginas[whitespace]desde)    -> captured as group 1
    # \d+                           -> one or more digits (to be removed)
    # ((-\d+)? )                   -> optional dash and number captured as group 2, if present
    pattern = r'(Paginas\s+desde)\d+((-\d+)?)'
    match = re.match(pattern, input_string)
    if match:
        # Reconstruct string using group 1 (the fixed prefix) and group 2 (the optional suffix)
        return (match.group(1) + match.group(2)).replace(" ", "")
    return input_string.replace(" ", "")