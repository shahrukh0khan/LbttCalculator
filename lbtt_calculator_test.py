import unittest
from lbtt_calculator import calculate_lbtt

class TestCalculateLbtt(unittest.TestCase):

    def test_lbtt(self):
        input_data = [0.0, -1, 145000.0, 250000, 325000, 750000.0, 800000, 140000.0, 150000.0, 300000.0, 450000.0, 156000.093, 144999.99, 145000.00001, 145000.1, 145001]
        
        expected_outputs = [0.0, 0.0, 0.0, 2100.0, 5850.0, 48350, 54350.0, 0.0, 100.0, 4600.0, 18350.0, 220.0, 0.0, 0.0, 0.0, 0.02]

        for i in range(0, len(input_data)):
            self.assertEquals(calculate_lbtt(input_data[i]), expected_outputs[i]) 

if __name__ == '__main__':
    unittest.main()

