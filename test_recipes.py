def tstplaceholder():
    assert True

from main import load_recipes, save_recipes

def test_load_recipes_empty(tmp_path):
    file = tmp_path / "recipes.txt"
    file.write_text("")
    recipes = load_recipes(file)
    assert recipes == []

def test_load_recipes_reads_lines(tmp_path):
    file = tmp_path / "recipes.txt"
    file.write_text("pasta\npizza\n")
    recipes = load_recipes(file)
    assert recipes == ["pasta","pizza"]

def test_save_recipes_writes_file(tmp_path):
    file = tmp_path / "recipes.txt"
    save_recipes(file, ["soup", "salad"])
    content = file.read_text()
    assert "soup" in content
    assert "salad" in content