# flake8: noqa: D101, D102
import importlib
import unittest

import matplotlib as mpl

import uastyle


class BasicTests(unittest.TestCase):
    def setUp(self) -> None:
        mpl.rcParams.update(mpl.rcParamsDefault)

    def check_colors(self):
        from uastyle import colors  # pylint: disable=C0415

        self.assertEqual(mpl.rcParams["axes.prop_cycle"].by_key()["color"][0], colors[0])

    def test_colors_import(self):
        from uastyle import colors  # pylint: disable=C0415, W0611

    def test_explicit_method(self):
        from uastyle import make_default_colors  # pylint: disable=C0415

        make_default_colors()

        self.check_colors()

    def test_import_method(self):
        from uastyle import apply_colors  # pylint: disable=C0415, W0611

        importlib.reload(apply_colors)

        self.check_colors()

    def test_import_from_apply(self):

        from uastyle.apply_colors import colors  # pylint: disable=C0415, W0611

        self.check_colors()


if __name__ == "__main__":
    unittest.main()
