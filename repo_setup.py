from pathlib import Path
from typing import List


def create_project_structure() -> None:
	"""Create the src/single_agent package scaffold for the agent project."""
	root: Path = Path(__file__).resolve().parent

	directories: List[Path] = [
		root / "src",
		root / "src" / "single_agent",
		root / "src" / "single_agent" / "agent",
		root / "src" / "single_agent" / "utils",
		root / "src" / "single_agent" / "config",
		root / "src" / "single_agent" / "prompts",
		root / "src" / "single_agent" / "tools",
		root / "src" / "single_agent" / "models",
		root / "src" / "single_agent" / "memory",
		root / "src" / "single_agent" / "workflows",
		root / "src" / "single_agent" / "state",
		root / "src" / "single_agent" / "evals",
		root / "src" / "single_agent" / "tests",
	]

	for directory in directories:
		directory.mkdir(parents=True, exist_ok=True)
		print(f"Created: {directory.relative_to(root)}")


if __name__ == "__main__":
	create_project_structure()