from typing import List

def main():
    num_elements = int(input())
    elements = [int(x) for x in input().split()]

    total_sum = sum(elements)
    if total_sum % 3 != 0:
        print(-1)
    else:
        partition_sum = total_sum // 3
        cumulative_sum = 0
        partition_indices = []
        for i in range(num_elements):
            cumulative_sum += elements[i]
            if cumulative_sum == partition_sum:
                partition_indices.append(i + 1)
                cumulative_sum = 0
            elif cumulative_sum > partition_sum:
                break

        if len(partition_indices) != 3:
            print(-1)
        else:
            print(partition_indices[0], partition_indices[1])

if __name__ == '__main__':
    main()
