from kivy.app import App
from kivy.uix.label import Label
import arabic_reshaper
import bidi.algorithm
import math
from kivy.core.window import Window

Window.size = (400, 800)
window_sizes=Window.size

def get_arabic_text(arabic_word, max_line_width, fixed_width):
    # Remove leading and trailing whitespace from the input Arabic word
    arabic_word = arabic_word.strip()
    
    # Check if the Arabic word is empty
    if len(arabic_word) <= 0:
        return ''
    
    # Reshape the Arabic word using arabic_reshaper module
    reshaped_word = arabic_reshaper.reshape(arabic_word)
    
    # Apply bidirectional algorithm to properly display the reshaped Arabic word
    display_word = bidi.algorithm.get_display(reshaped_word)
    
    # Check if either max_line_width or fixed_width is False or None
    if not max_line_width or not fixed_width:
        return display_word
    else:
        # Reverse the word list obtained from splitting the display_word by space
        reversed_word_list = display_word.split(' ')[::-1]
        
        # Check if the reversed_word_list is empty
        if len(reversed_word_list) == 0:
            return ''
        
        # Check if the reversed_word_list has only one word
        if len(reversed_word_list) == 1:
            return str(reversed_word_list[0])
        
        # Calculate the maximum number of characters per line
        max_chars = math.floor(max_line_width / fixed_width)
        
        # Iterate over the reversed_word_list
        for word in reversed_word_list:
            # Check if any word in the reversed_word_list exceeds the maximum number of characters per line
            if len(word) > max_chars:
                return display_word
        
        # Initialize a temporary string to store the formatted text
        temp_string = ''
        
        # Initialize a list to store the result lines
        result_list = []
        
        # Iterate over the reversed_word_list indices
        for i in range(0, len(reversed_word_list)):
            # Add a space before the current temporary string if it's not empty
            if temp_string != '':
                temp_string = ' ' + temp_string
            
            # Check if adding the current word to the temporary string exceeds the maximum number of characters per line
            if len(temp_string) + len(reversed_word_list[i]) > max_chars:
                # Add a newline character to the temporary string
                temp_string = temp_string + "\n"
                
                # Append the temporary string to the result list
                result_list.append(temp_string)
                
                # Reset the temporary string to the current word
                temp_string = reversed_word_list[i]
            else:
                # Add the current word to the temporary string
                temp_string = reversed_word_list[i] + temp_string
                
                # Check if it's the last word in the reversed_word_list
                if i == (len(reversed_word_list) - 1):
                    # Append the temporary string to the result list
                    result_list.append(temp_string)
        
        # Join the lines in the result list to form the final formatted text
        return ''.join(result_list)
  
# Defining a class
class MyFirstKivyApp(App):
      
    def build(self):

        tx = 'یادگیری ماشین، واژه‌ای است که توسط آرتور ساموئل در سال ۱۹۵۹ ابداع شد. این فناوری شاخه‌ای از هوش مصنوعی و علوم رایانه است. این تکنولوژی در علوم داده دارای اهمیت بسیار زیادی است.\
        یادگیری ماشین هوشمند کردن رایانه‌هاست بدون اینکه مستقیماً به آنها یاد بدهیم چطور رفتار کنند.\
        اما این اتفاق چطور می‌افتد؟ رایانه‌ها می‌توانند با استفاده از حجم عظیمی از داده، به طور خودکار الگوهایی تکرارشونده را بدون دخالت انسان یاد بگیرند. یادگیری این الگوریتم‌ها به تقلید از شیوه یادگیری انسان انجام می‌شود و با بیشتر شدن تجربه رایانه، به‌تدریج دقت آن بالاتر می‌رود.'

        #return Label(text = bidi.algorithm.get_display(arabic_reshaper.reshape(tx)), font_name= 'IRANSansXFaNum-Medium.ttf', base_direction= 'rtl', text_size= (window_sizes[0], None))

        return Label(text = get_arabic_text(tx, window_sizes[0], 7.5), font_name= 'IRANSansXFaNum-Medium.ttf', base_direction= 'rtl'     )   
  
  
MyFirstKivyApp().run()      