import sys
sys.path.append('../satisfy-calc')

from recipe import Recipe
from item import Item
import unittest

class Test_Recipe(unittest.TestCase):

    def setUp(self):
        self.input_item1 = Item('Input_Item_1', 'solid', 10)
        self.input_item2 = Item('Input_Item_2', 'solid', 20)
        self.output_item1 = Item('Output_Item_1', 'solid', 1)
        self.output_item2 = Item('Output_Item_2', 'solid', 2)

        self.inputs_list = [self.input_item1, self.input_item2]
        self.outputs_list = [self.output_item1, self.output_item2]

        self.recipe_name = 'Test_Recipe'
        self.building = 'Test_Building'
        self.is_alternate = False

        self.test_recipe = Recipe(self.recipe_name, self.inputs_list, self.outputs_list, self.building, self.is_alternate)

    def tearDown(self):
        pass

    def test_str(self):
        self.assertEqual(self.test_recipe.__str__(), f'Recipe name: {self.recipe_name}\nInputs: {self.test_recipe.input_names}\nOutputs: {self.test_recipe.output_names}\nMade in: {self.building}\nIs alt. recipe: {self.is_alternate}\n')

    def test_repr(self):
        self.assertEqual(self.test_recipe.__repr__(), f'Recipe for {self.recipe_name}')

    def test_scale_by(self):
        multiplier = 2.5

        irates_before = self.test_recipe.input_rates
        irates_before_multiplied = [multiplier*rate for rate in irates_before]
        orates_before = self.test_recipe.output_rates
        orates_before_multiplied = [multiplier*rate for rate in orates_before]

        self.test_recipe.scale_by(multiplier)

        irates_after = self.test_recipe.input_rates
        orates_after = self.test_recipe.output_rates

        self.assertEqual(irates_before_multiplied, irates_after)
        self.assertEqual(orates_before_multiplied, orates_after)

    def test_scale_inputs_by(self):
        multiplier = 1.45

        irates_before = self.test_recipe.input_rates
        irates_before_multiplied = [multiplier*rate for rate in irates_before]

        self.test_recipe.scale_by(multiplier)

        irates_after = self.test_recipe.input_rates

        self.assertEqual(irates_before_multiplied, irates_after)

    def test_scale_outputs_by(self):
        multiplier = 1236

        orates_before = self.test_recipe.output_rates
        orates_before_multiplied = [multiplier*rate for rate in orates_before]

        self.test_recipe.scale_by(multiplier)

        orates_after = self.test_recipe.output_rates

        self.assertEqual(orates_before_multiplied, orates_after)
    
    def test_summary(self):
        self.assertEqual(self.test_recipe.summary, f'[{self.recipe_name}] made from {self.test_recipe.list_formatter(self.test_recipe.input_names)}')

    def test_list_formatter(self):
        test_list = ['first', 'second', 'third']
        self.assertEqual(self.test_recipe.list_formatter(test_list), '[first, second, third]')

    def test_name(self):
        self.assertEqual(self.test_recipe.name, self.recipe_name)

        new_name = 'New_Recipe_Name'
        self.test_recipe.name = new_name
        self.assertEqual(self.test_recipe.name, new_name)

    def test_is_raw(self):
        self.assertFalse(self.test_recipe.is_raw)

        self.test_recipe.input_items = None
        self.assertTrue(self.test_recipe.is_raw)

    def test_input_items(self):
        inputs_from_recipe = self.test_recipe.input_items
        standalone_inputs = self.inputs_list

        self.assertEqual(len(inputs_from_recipe), len(standalone_inputs))

        for i1, i2 in zip(inputs_from_recipe, standalone_inputs):
            self.assertEqual(i1.name, i2.name)
            self.assertEqual(i1.form, i2.form)
            self.assertEqual(i1.rate, i2.rate)

    def test_input_names(self):
        inputs_from_recipe = self.test_recipe.input_items
        standalone_inputs = self.inputs_list

        self.assertEqual(len(inputs_from_recipe), len(standalone_inputs))

        for i1, i2 in zip(inputs_from_recipe, standalone_inputs):
            self.assertEqual(i1.name, i2.name)

    def test_input_rates(self):
        inputs_from_recipe = self.test_recipe.input_items
        standalone_inputs = self.inputs_list

        self.assertEqual(len(inputs_from_recipe), len(standalone_inputs))

        for i1, i2 in zip(inputs_from_recipe, standalone_inputs):
            self.assertEqual(i1.rate, i2.rate)

    def test_output_items(self):
        outputs_from_recipe = self.test_recipe.output_items
        standalone_outputs = self.outputs_list

        self.assertEqual(len(outputs_from_recipe), len(standalone_outputs))

        for o1, o2 in zip(outputs_from_recipe, standalone_outputs):
            self.assertEqual(o1.name, o2.name)
            self.assertEqual(o1.form, o2.form)
            self.assertEqual(o1.rate, o2.rate)

    def test_output_names(self):
        outputs_from_recipe = self.test_recipe.output_items
        standalone_outputs = self.outputs_list

        self.assertEqual(len(outputs_from_recipe), len(standalone_outputs))

        for o1, o2 in zip(outputs_from_recipe, standalone_outputs):
            self.assertEqual(o1.name, o2.name)

    def test_output_rates(self):
        outputs_from_recipe = self.test_recipe.output_items
        standalone_outputs = self.outputs_list

        self.assertEqual(len(outputs_from_recipe), len(standalone_outputs))

        for o1, o2 in zip(outputs_from_recipe, standalone_outputs):
            self.assertEqual(o1.rate, o2.rate)

    def test_building(self):
        self.assertEqual(self.test_recipe.building, self.building)

    def test_is_base(self):
        self.assertTrue(self.test_recipe.is_base)

    def test_is_alt(self):
        self.assertFalse(self.test_recipe.is_alt)
        self.test_recipe.is_alt = True
        self.assertTrue(self.test_recipe.is_alt)

    def test_get_input_item_from_name(self):
        returned_item = self.test_recipe.get_input_item_from_name(self.input_item1.name)
        self.assertIsInstance(returned_item, Item)
        self.assertEqual(returned_item.name, self.input_item1.name)

        returned_item = self.test_recipe.get_input_item_from_name(self.input_item2.name)
        self.assertIsInstance(returned_item, Item)
        self.assertEqual(returned_item.name, self.input_item2.name)

    def test_get_output_item_from_name(self):
        returned_item = self.test_recipe.get_output_item_from_name(self.output_item1.name)
        self.assertIsInstance(returned_item, Item)
        self.assertEqual(returned_item.name, self.output_item1.name)

        returned_item = self.test_recipe.get_output_item_from_name(self.output_item2.name)
        self.assertIsInstance(returned_item, Item)
        self.assertEqual(returned_item.name, self.output_item2.name)

    def test_get_ratio(self):
        for inp in self.inputs_list:
            for out in self.outputs_list:
                self.assertEqual(self.test_recipe.get_ratio(inp.name, out.name), inp.rate/out.rate)

    def test_get_ratio_rev(self):
        for inp in self.inputs_list:
            for out in self.outputs_list:
                self.assertEqual(self.test_recipe.get_ratio_rev(inp.name, out.name), out.rate/inp.rate)
    

if __name__ == '__main__':
    unittest.main()