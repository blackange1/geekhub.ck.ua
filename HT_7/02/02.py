import pathlib


class LengthChar(Exception):
   pass


class LimitCharsString(Exception):
   pass


class TypeChar(Exception):
   pass


def print_file_content(name_file, n, char='#')->None:
   res = None

   if not isinstance(char, str):
      raise TypeChar()
   
   elif len(char) != 1:
      raise LengthChar()
   
   with open(pathlib.Path(__file__).parent.joinpath(name_file), 'r') as file:
      line = file.read()
      len_string = len(line)

      if len_string < n:
         raise LimitCharsString()

      if len_string < n * 3:
         res = []
         start_idex_center_position = len_string // 2 - n // 2

         res.append(line[:n])
         res.append(line[start_idex_center_position: start_idex_center_position + n])
         res.append(line[-n:])
         res = ','.join(res)

      else:
         count_space = len_string - n * 3

         count_space_right = count_space // 2
         count_space_left = count_space - count_space_right

         start_index_center_element = n + count_space_left
         
         res = line[:n]
         res += '*' * count_space_left
         res += line[start_index_center_element: start_index_center_element + n]
         res += '*' * count_space_right
         res += line[-n:]

      print(res)


path_test = pathlib.Path(__file__).parent.joinpath('test')

tests = [
   ('test_1.txt', 3),
   ('test_1.txt', 4),
   ('test_1.txt', 5),

   ('test_2.txt', 3),
   ('test_2.txt', 4),
   ('test_2.txt', 8),
   
   ('test_3.txt', 4),
   ('test_3.txt', 5),
   ('test_3.txt', 6),
]

for path, n in tests:
   print_file_content(path_test.joinpath(path), n)
