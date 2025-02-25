import keyword

def display_data_types():
    """Prints different Python data types along with their types"""
    
    # Integer Data Type
    integer_value: int = 10  
    print("Integer:", integer_value, "| Type:", type(integer_value))

    # Float Data Type
    float_value: float = 60.5  
    print("Float:", float_value, "| Type:", type(float_value))

    # String Data Type
    string_value: str = "Hello to Python Journey!"  
    print("String:", string_value, "| Type:", type(string_value))

    # List Data Type
    list_value: list[int | str] = [1, 2, 3, "peach", "strawberry"]  
    print("List:", list_value, "| Type:", type(list_value))
    print("Last Element of List:", list_value[-1])
    print("First Element of List:", list_value[-5])
    print("Middle Element of List:", list_value[-3])

    # Tuple Data Type
    tuple_value: tuple = (10, 20, 30, "infinite")  
    print("Tuple:", tuple_value, "| Type:", type(tuple_value))

    # Set Data Type
    set_value: set = {1, 2, 3, 4, 5}  
    print("Set:", set_value, "| Type:", type(set_value))

    # FrozenSet Data Type (Immutable Set)
    frozenset_value: frozenset = frozenset({1, 2, 3, 4, 5})  
    print("Frozenset:", frozenset_value, "| Type:", type(frozenset_value))

    # Dictionary Data Type
    dict_value: dict[str, str] = {"name": "Hubab", "age": "25", "city": "Karachi"}  
    print("Dictionary:", dict_value, "| Type:", type(dict_value))
    print("City from Dictionary:", dict_value["city"])

    # Boolean Data Type
    boolean_value: bool = True  
    print("Boolean:", boolean_value, "| Type:", type(boolean_value))

    # NoneType Data Type
    none_value: None = None  
    print("NoneType:", none_value, "| Type:", type(none_value))

def display_keywords():
    """Prints Python keywords and soft keywords"""
    
    # Printing Python Keywords
    print("\nPython Keywords:")
    print(keyword.kwlist)

    # Printing Python Soft Keywords (Python 3.10+)
    print("\nPython Soft Keywords:")
    soft_keywords: list = ["match", "case", "type", "yield"]
    print(soft_keywords)
