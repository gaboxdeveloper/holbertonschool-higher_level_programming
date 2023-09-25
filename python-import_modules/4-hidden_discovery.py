#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    def print_module_names(hidden_4):
        module_names = dir(hidden_4)
        for name in sorted(module_names):
            if not name.startswith('__'):
                print(name)
