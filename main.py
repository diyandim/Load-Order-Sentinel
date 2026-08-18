from abc import ABC, abstractmethod
import argparse
import sys

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
        


def main(path: str):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(f"Could not find a file at '{path}'. Please check the path and try again.")
        sys.exit(1)

    collected_plugins = []

    for plugin in f:
        stripped = plugin.strip()
        if stripped == "":
            continue
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

class MalformedRule(Rule):
    def check(self, plugins: list[Plugin]):
        malformed_plugins = []

        for y in plugins:
            if not y.name.endswith((".esp", ".esm", ".esl")):
                malformed_plugins.append(f"{y.name}: Invalid file extension")

        return malformed_plugins

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="plugins.txt")
    args = parser.parse_args()

    all_plugins = main(args.path)
    combined = {
        
    }

    rules = [
    DuplicateRule(),
    ConflictRule(),
    MalformedRule(),
    ]
    for rule in rules:
        findings = rule.check(all_plugins)
        combined[rule.__class__.__name__] = findings

    for rule_name, rule_findings in combined.items():
        print(f"{rule_name}:")
        if rule_findings:
            for finding in sorted(rule_findings):
                print(f"  {finding}")
        else:
            print("  No issues found.")