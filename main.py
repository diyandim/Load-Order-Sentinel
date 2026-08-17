
class Plugin():
    def __init__(self, name: str, enabled: bool):
        self.name = name
        self.enabled = enabled

    def __repr__(self):
        return f"Plugin(name={self.name}, enabled={self.enabled})"

def main():
    f = open("plugins.txt", "r")
    collected_plugins = []

    for plugin in f:
        stripped = plugin.strip()
        is_enabled = stripped.startswith("*")
        clean_name = stripped.strip("*")
        collected_plugins.append(Plugin(clean_name, is_enabled))

    f.close()
    print(collected_plugins)
    return collected_plugins

def find_duplicates(plugins: list[Plugin]):
    seen_names = []
    duplicate_names = []

    for plug in plugins:
        if plug.name in seen_names:
            duplicate_names.append(plug.name)
        else:
            seen_names.append(plug.name)

    return duplicate_names

if __name__ == "__main__":
    all_plugins = main()
    duplicates = find_duplicates(all_plugins)
    print(duplicates)