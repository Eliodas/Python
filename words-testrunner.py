import unittest

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromName("nowordtest"))

runner = unittest.TextTestRunner()
runner.run(suite)