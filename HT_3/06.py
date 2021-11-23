"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""

def abracadabra(string):
   len_s = len(string)
   
   def alpha_and_digit(s) -> tuple:
      string_str, digit_list = '', []
      container_n = ''
      s = s + ' '
      for ch in s:
         if ch.isdigit():
            container_n += ch
         elif ch.isalpha():
            if container_n:
               digit_list.append(int(container_n))
               container_n = ''
            string_str += ch
         else:
            if container_n:
               digit_list.append(int(container_n))
               container_n = ''
      return string_str, digit_list


   if len_s < 30:
      s, numbers = alpha_and_digit(string)
      print('sum(numbers) =', sum(numbers))
      print('all_letters =', s)
   elif len_s <= 50:
      s, numbers = alpha_and_digit(string)
      print('len(chs) =', len(s))
      print('len(numbers) =', len(numbers))
   else:
      d = {}
      for ch in string:
         if ch in d:
            d[ch] += 1
         else:
            d[ch] = 1      
      for key, value in sorted(d.items(), key=lambda t: t[1], reverse=True):
         print(f"'{key}': {value}", end=', ')
      print()


abracadabra('f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345')
print()
abracadabra('f98neroi4nr0c3n30irn03ien3c0rfekdno40') # 98 4 0 3 30 3 3 0 40 -> 9
print()
abracadabra('f98neroi4nr0c3n30irn03ien3c0r') # 98 + 4 + 0 + 3 + 30 + 3 + 3 + 0 = 141 
