"""Integration tests for rocket simulator

To run these tests:
    python test.py -v
    
Or with specific test:
    python -m pytest test.py::Software::test_1 -v

Or
    python -m unittest test.Software.test_1
"""

import waterRocketSim as wrs

import traceback
import unittest
import sys
import time
from functools import wraps
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
       
class TestSoftware(unittest.TestCase):
    """Test utils functions."""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def test_1(self):
        rocket=wrs.WaterRocket()
        flyParameters = rocket.launchSimulation()

        print("\nTest 1: dfsghstfhsfthfgh")
        #self.assertEqual()

def print_test_instructions():
    """Print instructions for running software tests."""
    print("\n" + "="*70)
    print("ROCKET SIMULATOR SOFTWARE TEST SUITE")
    print("="*70)
    print("\nRunning all tests:")
    print("  python test.py -v")
    print("\nRunning specific test class:")
    print("  python -m pytest test.py::Software -v")
    print("\nRunning specific test:")
    print("  python -m pytest test.py::Software::test_1 -v")
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    print_test_instructions()
    unittest.main(verbosity=2)
