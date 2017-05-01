from argparse import ArgumentParser
from re import sub
from itertools import count
from math import ceil
import os
import re
import sys
import collections
sys.setrecursionlimit(100000)


diff_deque = collections.deque([[-1, 0],
                                [-1, 1],
                                [0, 1],
                                [1, 1],
                                [1, 0],
                                [1, -1],
                                [0, -1],
                                [-1, -1]])
diff_dict = {}
diff_dict[-1, 0] = 0
diff_dict[-1, 1] = 1
diff_dict[0, 1] = 2
diff_dict[1, 1] = 3
diff_dict[1, 0] = 4
diff_dict[1, -1] = 5
diff_dict[0, -1] = 6
diff_dict[-1, -1] = 7
def main():
    parser = ArgumentParser()
    parser.add_argument('--file', dest='file', required=True)
    parser.add_argument('-print', action='store_true', required=False)
    args = parser.parse_args()

    file_name = args.file

    input_matrix = {}
    visited_matrix = {}
    row_length = 0
    column_length = 0
    try:
        with open(file_name, 'r') as txt_file:
            for line in txt_file:
                line = line.replace('\n', '').replace(' ', '')
                if len(line) == 0:
                    continue
                current = list(line)
                current_index = 0

                for i in range(0, len(current)):

                    if current[i].lstrip().rstrip() == '' :
                        input_matrix[row_length, i, i] = '0'
                    else:
                        input_matrix[row_length, i] = current[i]
                    visited_matrix[row_length, i] = False


                column_length = max(len(current), column_length)
                row_length += 1


            changed_number = ord('A')
            for i in range(row_length):
                for j in range(column_length):
                    print(input_matrix[i, j], end = '')
                print()
            for i in range(row_length):
                for j in range(column_length):

                    visited = visited_matrix.copy()  
                    if input_matrix[i, j] == '1' and visited[i, j] == False:
                        input_matrix[i, j] = chr(changed_number)
                        result = list()
                        results = list()
                        for index in range(2, 5):
                            new_x = i + diff_deque[index][0]
                            new_y = j + diff_deque[index][1]
                            find_path(i, j, i + diff_deque[index][0], j + diff_deque[index][1], diff_dict[diff_deque[index][0], diff_deque[index][1]], row_length, column_length,
                                      visited, input_matrix, result, results)
                            if len(results) > 0:
                                break


                        max_val = list()
                        for val in results:
                            if len(val) > len(max_val):
                                max_val = val
                        if len(max_val) == 0:
                            continue
                        for value in max_val:
                            input_matrix[value[0], value[1]] = chr(changed_number)
                            visited_matrix[value[0], value[1]] = True
                        changed_number += 1
            for i in range(row_length):
                for j in range(column_length):
                    print(input_matrix[i, j], end= '')
                print()



    except ValueError:
        print('Incorrect input.')
        sys.exit()

def find_path(dest_x, dest_y,
              source_x, source_y,
              direction,
              row_length,
              column_length,
              visited,
              input_matrix, result, results):
    if len(results) > 0:
        return
    if dest_x == source_x and dest_y == source_y:
        new_result = result[0:]
        results.append(new_result)
        return
    if source_x < 0 or source_x >= row_length:
        return
    if source_y < 0 or source_y >= column_length:
        return

    if visited[source_x, source_y]:
        return;
    if input_matrix[source_x, source_y] == '1':
        #[[-1, 0],[-1, 1],[0, 1],[1, 1],[1, 0],[1, 1],[0, -1],[-1, -1]])
        new_diff = collections.deque(diff_deque)
        temp_x = source_x
        temp_y = source_y
        temp_direction = direction
        #new_diff.rotate(-1 * direction)
        result.append([source_x, source_y])
        visited[source_x, source_y] = True
        #(calculate_direction(new_diff[index_diff][0], new_diff[index_diff][0], diff_deque)) % 8

        find_path(dest_x, dest_y, source_x + new_diff[0][0], source_y + new_diff[0][1],
                  diff_dict[new_diff[0][0], new_diff[0][1]] , row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[1][0], source_y + new_diff[1][1],
                  diff_dict[new_diff[1][0], new_diff[1][1]], row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[2][0], source_y + new_diff[2][1],
                  diff_dict[new_diff[2][0], new_diff[2][1]], row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[3][0], source_y + new_diff[3][1],
                  diff_dict[new_diff[3][0], new_diff[3][1]], row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[4][0], source_y + new_diff[4][1],
                  diff_dict[new_diff[4][0], new_diff[4][1]], row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[5][0], source_y + new_diff[5][1],
                  diff_dict[new_diff[5][0], new_diff[5][1]], row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[6][0], source_y + new_diff[6][1],
                  diff_dict[new_diff[6][0], new_diff[6][1]], row_length, column_length, visited, input_matrix, result,
                  results)
        find_path(dest_x, dest_y, source_x + new_diff[7][0], source_y + new_diff[7][1],
                  diff_dict[new_diff[7][0], new_diff[7][1]], row_length, column_length, visited, input_matrix, result,
                  results)

        visited[source_x, source_y] = False
        del result[-1]


def calculate_direction(x, y, current_deque):
    return diff_dict[x, y]
main()