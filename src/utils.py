import re
import unicodedata

conversion_dict = {
    'empty': 'ORS-Otros',
    'Paginasdesde': 'CC-Cobertura',
    'Paginasdesde-2': "ActayRecepcion",
    'Paginasdesde-3': "CVC-CodigoValidacion",
    'Paginasdesde-4': "053-Derivacion",
    'Paginasdesde-5': "Inf-Medico",
}

def remove_accents(input_str):
    """
    Removes accent characters from the input string.
    """
    normalized = unicodedata.normalize('NFD', input_str)
    return "".join(c for c in normalized if unicodedata.category(c) != 'Mn')

def transform_pd_code(input_string):
    """
    Removes the number after "Paginas desde" from the input string
    after removing accent characters.
    
    Examples:
        "Páginas desde2567-2" -> "Paginasdesde-2"
        "Paginas desde2567"   -> "Paginasdesde"
    
    Args:
        input_string (str): The input string to transform.
    
    Returns:
        str: The transformed string if a match is found; otherwise, the original string with spaces removed.
    """
    if not input_string:
        return input_string.replace(" ", "")
    
    # Remove accents so that the regex can match correctly
    input_string = remove_accents(input_string)
    
    # Pattern:
    # (Paginas[whitespace]desde)   -> captured as group 1
    # \d+                          -> digits to remove
    # ((-\d+)? )                  -> optional dash and number captured as group 2, if present
    pattern = r'(Paginas\s+desde)\d+((-\d+)?)'
    match = re.match(pattern, input_string)
    if match:
        return (match.group(1) + match.group(2)).replace(" ", "")
    return input_string.replace(" ", "")