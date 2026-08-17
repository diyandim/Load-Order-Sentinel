from main import Plugin, DuplicateRule

def test_finds_duplicate_plugin():
    plugin_one = Plugin("SomeName.esp", True)
    plugin_two = Plugin("SomeName.esp", True)
    test_plugins = [plugin_one, plugin_two]
    result = DuplicateRule().check(test_plugins)
    assert "SomeName.esp" in result