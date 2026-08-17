
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


if __name__ == "__main__":
    main()