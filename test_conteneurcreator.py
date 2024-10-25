import pytest
import platform

from conteneurcreator import is_docker_installed

def test_system_detection():
  system = platform.system()
  assert system in ["Linux", "Windows"]
  
def test_docker_installed():
  result = is_docker_installed()
  assert isinstance(result, bool)
