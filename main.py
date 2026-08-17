
def main():
    f = open("plugins.txt", "r")
    for plugin in f:
        print(plugin.strip())
    f.close()
if __name__ == "__main__":
    main()