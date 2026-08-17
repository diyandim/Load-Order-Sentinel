from abc import ABC, abstractmethod

KNOWN_CONFLICTS = {
    "AnotherMod.esp": "Conflicts with SkyrimUI.",
    "SkyrimUI.esp": "Conflicts with AnotherMod.",
    "Ordinator.esp": "Conflicts with Apocalypse.",
    "RelationshipDialogueOverhaul.esp": "Conflicts with InterestingNPCs.",
    "Campfire.esp": "Conflicts with Frostfall.",
    "OpenCitiesSkyrim.esp": "Conflicts with city overhauls.",
    "LegacyoftheDragonborn.esp": "Conflicts with item overhauls.",
    "SomeTestMod.esp": "Conflicts with AnotherMod.",
    "DisabledExample.esp": "Causes UI conflicts.",
    "EnabledExample.esp": "Conflicts with Ordinator.",
}

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
    return collected_plugins

class Rule(ABC):
    @abstractmethod
    def check(self, plugins: list[Plugin]):
        pass

class DuplicateRule(Rule):
    def check(self, plugins: list[Plugin]):
        seen_names = []
        duplicate_names = []

        for plug in plugins:
            if plug.name in seen_names:
                duplicate_names.append(plug.name)
            else:
                seen_names.append(plug.name)

        return duplicate_names

class ConflictRule(Rule):
    def check(self, plugins: list[Plugin]):
        conflict_plugins = []

        for x in plugins:
            if x.name in KNOWN_CONFLICTS:
                conflict_plugins.append(f"{x.name}: {KNOWN_CONFLICTS[x.name]}")

        return conflict_plugins

if __name__ == "__main__":
    all_plugins = main()
    checked_plugins = []
    rules = [
    DuplicateRule(),
    ConflictRule(),
    ]
    for rule in rules:
        findings = rule.check(all_plugins)
        checked_plugins.extend(findings)

    print(checked_plugins)
