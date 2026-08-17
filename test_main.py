from main import Plugin, DuplicateRule, ConflictRule

def test_finds_duplicate_plugin():
    plugin_one = Plugin("SomeName.esp", True)
    plugin_two = Plugin("SomeName.esp", True)
    test_plugins = [plugin_one, plugin_two]
    result = DuplicateRule().check(test_plugins)
    assert "SomeName.esp" in result

def test_conflict_rule_plugin():
    plugin_one = Plugin("Ordinator.esp", True)
    plugin_two = Plugin("SkyrimUI.esp", True)
    plugin_three = Plugin("ImmersiveArmors.esp", True)
    plugin_four = Plugin("Campfire.esp", True)
    test_plugins = [plugin_one, plugin_two, plugin_three, plugin_four]
    result = ConflictRule().check(test_plugins)
    assert "Ordinator.esp: Conflicts with Apocalypse." in result
    assert "SkyrimUI.esp: Conflicts with AnotherMod." in result
    assert "Campfire.esp: Conflicts with Frostfall." in result
    assert "ImmersiveArmors.esp" not in str(result)