import Tests as t
import Plots as p
import os

input_directory = "Input"
output_directory = "Output"


input_file_N = os.path.join(input_directory, 'InputRange.txt')
input_file_M = os.path.join(input_directory, 'InputLimit.txt')
input_file = os.path.join(input_directory, 'Input.txt')

output_file_N = os.path.join(output_directory, 'OutputRange.txt')
output_file_M = os.path.join(output_directory, 'OutputLimit.txt')
output_file = os.path.join(output_directory, 'Output.txt')

Tests_N = t.read_tests(input_file_N)
Tests_M = t.read_tests(input_file_M)
Tests = t.read_tests(input_file)

Times_N, N_values, _ = t.perform_test_and_write_output(Tests_N, output_file_N)
Times_M, _, M_values = t.perform_test_and_write_output(Tests_M, output_file_M)
Times_N_M, N, M = t.perform_test_and_write_output(Tests, output_file)

# p.plot_performance(Times_N, N_values, Times_M, M_values)

# p.plot_surfaces()

#
