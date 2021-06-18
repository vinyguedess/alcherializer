import os
import sys
from unittest import defaultTestLoader, TextTestRunner


project_path: str = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.insert(0, project_path)

runner = TextTestRunner()
context = runner.run(defaultTestLoader.discover('tests'))

os.environ["TEST_EXIT_CODE"] = "0" if context.wasSuccessful() else "1"
sys.exit(not context.wasSuccessful())
