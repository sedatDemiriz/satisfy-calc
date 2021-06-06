import sys
sys.path.append('../satisfy-calc')

from item import Item
import unittest

class Test_Item(unittest.TestCase):

    def setUp(self):
        self.test_item_name = 'Test_Item_Name'
        self.test_item_form = 'solid'
        self.test_item_rate = 10
        
        self.test_item = Item(self.test_item_name, self.test_item_form, self.test_item_rate)

        self.str_gas = 'gas'
        self.str_liquid = 'liquid'
        self.str_solid = 'solid'

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.test_item._name, self.test_item_name)

    def test_str(self):
        self.assertEqual(self.test_item.__str__(), f'{self.test_item_rate}/min {self.test_item_name}.')
    
    def test_repr(self):
        self.assertEqual(self.test_item.__repr__(), f'Item(name=\'{self.test_item_name}\', form=\'{self.test_item_form}\', rate={self.test_item_rate})')

    def test_add(self):
        test_item2 = Item('Test_Item_Name', 'solid', 20)
        added_item = self.test_item + test_item2

        self.assertEqual(added_item.name, self.test_item.name)
        self.assertEqual(added_item.name, test_item2.name)
        self.assertEqual(added_item.form, self.test_item.form)
        self.assertEqual(added_item.form, test_item2.form)
        self.assertEqual(added_item.rate, self.test_item.rate + test_item2.rate)

    def test_name(self):
        self.assertEqual(self.test_item.name, self.test_item_name)
        
        temp_name = 'Temp_name'
        self.test_item.name = temp_name
        self.assertEqual(self.test_item.name, temp_name)

    def test_form(self):
        self.assertEqual(self.test_item.form, self.test_item_form)
        
        temp_form = 'Temp_form'
        self.test_item.form = temp_form
        self.assertEqual(self.test_item.form, temp_form)

    def test_rate(self):
        self.assertEqual(self.test_item.rate, self.test_item_rate)
        
        temp_rate = 12
        self.test_item.rate = temp_rate
        self.assertEqual(self.test_item.rate, temp_rate)

    def test_is_solid(self):
        self.test_item.form = self.str_solid
        self.assertTrue(self.test_item.is_solid)
        
        self.test_item.form = self.str_liquid
        self.assertFalse(self.test_item.is_solid)

        self.test_item.form = self.str_gas
        self.assertFalse(self.test_item.is_solid)
    
    def test_is_liquid(self):
        self.test_item.form = self.str_solid
        self.assertFalse(self.test_item.is_liquid)
        
        self.test_item.form = self.str_liquid
        self.assertTrue(self.test_item.is_liquid)

        self.test_item.form = self.str_gas
        self.assertFalse(self.test_item.is_liquid)

    def test_is_gas(self):
        self.test_item.form = self.str_solid
        self.assertFalse(self.test_item.is_gas)
        
        self.test_item.form = self.str_liquid
        self.assertFalse(self.test_item.is_gas)

        self.test_item.form = self.str_gas
        self.assertTrue(self.test_item.is_gas)

    def test_scale_by(self):
        multiplier = 2
        rate_before = self.test_item.rate
        self.test_item = self.test_item.scale_by(multiplier)
        rate_after = self.test_item.rate

        self.assertEqual(rate_after, rate_before*multiplier)


if __name__ == '__main__':
    unittest.main()