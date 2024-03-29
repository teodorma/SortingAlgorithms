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
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/999c098b-3799-486a-862d-c71ee6dbea55" width = 100%>
<p>Performance by Array Size(N) from 100000 to 900000</p>      

<p>Performance by Max Value(M) from 100000 to 900000</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/aad8aab7-6c2e-4aff-abbb-3b277ffa2e31" width = 100%>
<p>Performance by Array Size(N) from 1000000 to 9000000</p>        

<p>Performance by Max Value(M) from 1000000 to 9000000</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/5d362594-7928-4c90-a8bd-51e0d053c3b1" width = 100%>

<p>Performance by Array Size(N) from 10000000 to 90000000</p>  

<p>Performance by Max Value(M) from 10000000 to 90000000</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/482228cd-bd46-460e-809a-58c57d1d4f71" width = 100%>






### Performance by Data Distribution
<p>Radix Sort base 10 and base 2^16</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/ff1486b7-61dd-4ea0-b03b-2e632c60f1d4" width = 49%>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/6844d22b-c632-4f82-bc80-a8117474e8d3" width = 49%>
<p>Merge Sort and Shell Sort</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/f9e0d40f-510e-444a-9939-1d937e21e537" width = 49%>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/1d84dd39-2868-4abc-887c-772fd9c6d5d2" width = 49%>
<p>Cube Sort and Bucket Sort</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/a691f9c3-acca-4a89-a91c-c1c6120803a1" width = 49%>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/9cab0bc9-8d1a-42f6-b841-66c1487e01d3" width = 49%>
<p>Heap Sort and Native Sort</p>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/5f2390df-70a7-4984-9dbe-64e4c1e7b8a6" width = 49%>
<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/e7f76b68-2daa-4e97-8189-f9408e94ce86" width = 49%>

<img src = "https://github.com/teodorma/SortingAlgorithms/assets/127875348/c4f52a81-a468-4d5a-8388-180ddf6f6d77" width = 98%>


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

