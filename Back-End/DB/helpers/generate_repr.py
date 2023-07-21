def generate_repr(name: str, key_dict: dict):
    gen_str = ""

    for k in list(key_dict.keys()):
        gen_str += f"\n\t{k}:\t\t{key_dict[k]}"

    return f"{name}({gen_str}\n)"