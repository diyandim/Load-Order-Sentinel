
def main():
    f = open("plugins.txt", "r")
    collected_plugins = []
    for plugin in f:
        collected_plugins.append(plugin.strip())
    f.close()
    print(collected_plugins)
    return collected_plugins
    

if __name__ == "__main__":
    main()

