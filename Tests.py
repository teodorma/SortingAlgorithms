import random
import time
import Sorting_Algorithms as sr

SORTING_ALG = {
    "radix_sort_base10": sr.radix_sort_base10,
    "radix_sort_base2_16": sr.radix_sort_base2_16,
    "merge_sort": sr.merge_sort,
    "shell_sort": sr.shell_sort,
    "cube_sort": sr.cube_sort,
    "bucket_sort": sr.bucket_sort,
    "heap_sort": sr.heap_sort,
    "native_sort": sr.native_sort
}
sorting_algorithms = list(SORTING_ALG.keys())


def read_tests(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        tests = [(int(x), int(y)) for x, y in [line.split() for line in lines]]
    return tests


def perform_test_and_write_output(tests, output_filename):
    Times = {sort_name: [] for sort_name in sorting_algorithms}
    N_values, M_values = [], []
    try:
        with open(output_filename, "w") as f:
            for N, M in tests:
                Numbers = [random.uniform(0, M) for _ in range(N)]
                N_values.append(N)
                M_values.append(M)
                f.write(f"Test: N={N}, M={M}\n")

                for sort_name in sorting_algorithms:
                    start_time = time.time()
                    sorted_array = SORTING_ALG[sort_name](Numbers)

                    if sorted_array is None:
                        sorted_array = Numbers
                    status = "OK" if sr.test_sorted(sorted_array) else "Failed"
                    elapsed_time = time.time() - start_time
                    Times[sort_name].append(elapsed_time)

                    f.write(f"{sort_name}: {elapsed_time} seconds status {status}\n")
                f.write("\n")
    except:
        Times[sort_name] = []
        print("Error")
    return Times, N_values, M_values

