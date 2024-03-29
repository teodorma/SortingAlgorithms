# Sorting Algorithms Performance Comparison

## Introduction

This project explores the performance of several well-known sorting algorithms across different datasets. The aim is to understand how each algorithm behaves under various conditions and identify their strengths and weaknesses. This analysis can guide algorithm selection in practical software development scenarios where sorting efficiency can significantly impact application performance.

## Algorithms Under Test

We compare the performance of the following seven sorting algorithms:

- **Radix Sort**: Implemented in two variants based on different bases:
  - Base 10
  - Base 2^16
- **Merge Sort**: A classic divide-and-conquer algorithm known for its efficiency and stability.
- **Shell Sort**: An in-place comparison sort that generalizes insertion sort to allow the exchange of far-apart elements.
- **Cube Sort**: A sorting algorithm that improves upon the performance of bubble sort.
- **Bucket Sort**: A distribution sort that distributes elements into buckets and then sorts these buckets.
- **Heap Sort**: Based on a binary heap data structure, it's an in-place sort with no quadratic worst-case scenarios.
- **Python's Native Sort Function**: Utilizes Tim Sort, a hybrid stable sorting algorithm derived from merge sort and insertion sort.

## Performance Evaluation

To evaluate the performance of these sorting algorithms, we conducted a series of tests varying the size and distribution of the datasets. Below are the graphs showcasing the algorithms' execution times as a function of dataset size and complexity.

### Performance by Array Size and Max Value
<p>Performance by Array Size(N) from 10000 to 90000</p>

<p>Performance by Max Value(M) from 10000 to 90000</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/babc836b-9646-41ab-bacc-1f24c182fdcb" width = 100%>
<p>Performance by Array Size(N) from 100000 to 900000</p>      

<p>Performance by Max Value(M) from 100000 to 900000</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/c915edf6-0202-40e4-80a3-8906772d5489" width = 100%>
<p>Performance by Array Size(N) from 1000000 to 9000000</p>        

<p>Performance by Max Value(M) from 1000000 to 9000000</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/228c8bb4-79f9-4f22-9808-7bea2e382118" width = 100%>


<p>Performance by Array Size(N) from 10000000 to 90000000</p>     
<p>Performance by Max Value(M) from 10000000 to 90000000</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/482228cd-bd46-460e-809a-58c57d1d4f71" width = 100%>


### Performance by Data Distribution
<p>Radix Sort base 10 and base 2^16</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/fac6107d-c3d8-4153-90ac-d78b0bf0e4d5" width = 49%>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/0cacbe6a-e51f-426a-b747-f7828fe67084" width = 49%>
<p>Merge Sort and Shell Sort</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/6cf7aed9-0dd6-4e9e-9bd4-0ba7482750eb" width = 49%>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/07d42149-b42c-41ed-b5e1-592cf24e1f6c" width = 49%>
<p>Cube Sort and Bucket Sort</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/addc6176-b12c-4638-b14a-6c09623462ca" width = 49%>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/1c31a178-522c-47c1-af8e-7ff81d141c3f" width = 49%>
<p>Heap Sort and Native Sort</p>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/a235e2dd-af43-4076-a8d2-f7a21f84a889" width = 49%>
<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/aafbecc0-2c39-4516-91e2-7914e8301362" width = 49%>

<img src = "https://github.com/teodorma/Sorting_Algorithms/assets/108132918/40c9708f-6276-4140-a89d-85d723e68834" width = 98%>


## Key Findings

- **Radix Sort**: Shows great performance on large datasets when using a base of 2^16, which aligns well with modern computer architecture.However, its performance significantly deteriorates when the radix base is set to 10, highlighting a notable weakness in its efficacy for sorting operations involving base 10 representations.
- **Merge Sort**: Consistently good performance, demonstrating its utility as a general-purpose sorting algorithm.
- **Cube Sort**: Stands out as one of the most efficient sorting algorithms, particularly excelling in scenarios where dataset sizes vary and the distribution of elements fluctuates.
- **Shell Sort**: Demonstrates versatility and resilience in adapting to changes in array size and fluctuations in the maximum values of elements, showcasing consistent effectiveness across diverse datasets.
- **Bucket Sort**: Emerges as a powerful sorting algorithm, adept at efficiently organizing data with varying distributions and sizes.
- **Heap Sort**: Exhibits satisfactory performance in scenarios where array size remains constant, but reveals weaknesses when array size fluctuates. However, it demonstrates competency when tasked with sorting data sets where the maximum values of the elements vary significantly.
- **Python's Native Sort**: The Tim Sort algorithm shows outstanding versatility and efficiency, making it a robust choice for a wide range of applications.


## Conclusion

This comparative analysis reveals the nuanced performances of various sorting algorithms under different conditions. Understanding these characteristics enables developers to make informed decisions when choosing an algorithm for their specific needs, optimizing for factors such as execution time, memory usage, and stability.

