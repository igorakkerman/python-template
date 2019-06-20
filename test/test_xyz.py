from unittest import TestCase

import pytest

from xyz.xyz import xyz


class TestXyz(TestCase):

    def test_empty(self):
        with pytest.raises(ValueError, match="List must not be empty."):
            xyz([])

    def test_single(self):
        assert xyz([1]) == 1