import os

from blender_wrapper.blender_wrapper import get_script_path


def test_script_mapping():
    assert os.path.isfile(get_script_path('array_objects_by_curve'))
