import tkinter as tk
from tkinter import ttk
import random
import re

def convert_to_haxyn_style(text):
    if not text:
        return ""
    
    # Pre-processing: remove spaces more aggressively for short phrases
    if len(text) < 10 and random.random() < 0.4:
        text = text.replace(" ", "")
    elif random.random() < 0.15:
        text = text.replace(" ", "")
        
    words = text.split()
    converted_words = []
    
    # 1. Start with specific starters
    if random.random() < 0.25:
        starter = random.choice(['ㅇㄴ', 'ㅅㅂ', '아니', '근데', '왁'])
        converted_words.append(starter)

    for word in words:
        # 2. Base replacements & Intensifiers
        word = word.replace('진짜', 'ㅈㅉ')
        word = word.replace('너무', 'ㅈㄴ')
        word = word.replace('정말', 'ㅈㅉ')
        word = word.replace('매우', '개')
        word = word.replace('엄청', '개')
        word = word.replace('싫다', '실어')
        word = word.replace('싫어', '실어')
        word = word.replace('좋아', '조ㅎ아')
        word = word.replace('맞아', 'ㅇㅈ')
        word = word.replace('인정', 'ㅇㅈ')
        word = word.replace('그러니까', 'ㄱㄴㄲ')
        word = word.replace('많아', '만아')
        word = word.replace('뭐지', '머지')
        word = word.replace('뭐야', '머ㅑㅇ')
        word = word.replace('새끼들', '새키들')
        
        # 3. Particle/Ending shorthand
        word = word.replace('있어', '잇서')
        word = word.replace('있음', '잇슴')
        word = word.replace('했어', '햇서')
        word = word.replace('잖아요', '잔아여')
        
        # 4. Ending variations
        if word.endswith('어'):
            r = random.random()
            if r < 0.2: word = word[:-1] + '더'
            elif r < 0.4: word = word[:-1] + '어어'
            elif r < 0.5: word = word[:-1] + 'ㅛㅇ어'
            elif r < 0.6: word = word[:-1] + '햇슨'
        elif word.endswith('다'):
            r = random.random()
            if r < 0.3: word = word[:-1] + '타'
            elif r < 0.6: word = word[:-1] + '어'
        elif word.endswith('해'):
            r = random.random()
            if r < 0.3: word = word[:-1] + '핸더'
            elif r < 0.6: word = word[:-1] + '해어'
        elif word.endswith('요'):
            if random.random() < 0.5: word = word[:-1] + 'ㅛㅇ'
            
        # 5. Typos / Extra consonants (more subtle)
        if len(word) > 2 and random.random() < 0.1:
            idx = random.randint(0, len(word)-1)
            char = word[idx]
            if '가' <= char <= '힣':
                word = word[:idx+1] + random.choice(['ㄱ', 'ㄴ', 'ㅇ']) + word[idx+1:]

        # 6. Specific word replacements
        if word in ['응', '어', '어어']: word = '운'
        elif word == '아니': word = 'ㅇㄴ'
            
        # 7. Trailing marks (only at the end of the whole text usually, or rare)
        if word == words[-1] and random.random() < 0.15:
            word += random.choice(['!', '?', 'ㅋㅋㅋㅋ', 'ㅎㅎㅎ'])
            
        converted_words.append(word)
    
    # 8. Join logic (mostly spaces, but occasionally none)
    result = "".join(converted_words) if random.random() < 0.15 else " ".join(converted_words)
    
    # 9. Add emotional emojis & laughter (balanced)
    r_emo = random.random()
    if r_emo < 0.08: # Crying is less frequent now
        result += "ㅜ" * random.randint(2, 4)
    elif r_emo < 0.12:
        result += "ㅠ" * random.randint(2, 4)
    elif r_emo < 0.45: # Laughter is very frequent
        result += " " + "ㅋ" * random.randint(3, 10)
    elif r_emo < 0.55:
        result += " " + "ㅎ" * random.randint(3, 5)
        
    # 10. Opinion # prefix
    if random.random() < 0.12:
        result = "# " + result

    return result

class HaxynConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("haxyn._.s2 말투 변환기")
        self.root.geometry("500x400")
        self.root.configure(bg="#36393f") # Discord-like dark theme
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", foreground="#dcddde", background="#36393f", font=("Malgun Gothic", 10))
        style.configure("TButton", font=("Malgun Gothic", 10, "bold"))
        
        # Header
        self.header_label = tk.Label(root, text="haxyn._.s2 말투 변환기", font=("Malgun Gothic", 16, "bold"), 
                                   fg="white", bg="#2f3136", pady=10)
        self.header_label.pack(fill=tk.X)
        
        # Input Section
        self.input_label = ttk.Label(root, text="변환할 말을 입력하세요:")
        self.input_label.pack(pady=(20, 5))
        
        self.input_text = tk.Text(root, height=5, font=("Malgun Gothic", 11), bg="#40444b", fg="white", 
                                insertbackground="white", relief=tk.FLAT)
        self.input_text.pack(padx=20, fill=tk.X)
        
        # Convert Button
        self.convert_button = tk.Button(root, text="말투 변환하기 ✨", command=self.on_convert, 
                                      bg="#5865f2", fg="white", font=("Malgun Gothic", 11, "bold"), 
                                      relief=tk.FLAT, activebackground="#4752c4", activeforeground="white",
                                      cursor="hand2")
        self.convert_button.pack(pady=15)
        
        # Output Section
        self.output_label = ttk.Label(root, text="haxyn._.s2의 말투:")
        self.output_label.pack(pady=(5, 5))
        
        self.output_text = tk.Text(root, height=5, font=("Malgun Gothic", 11), bg="#2f3136", fg="skyblue", 
                                 relief=tk.FLAT, state=tk.DISABLED)
        self.output_text.pack(padx=20, fill=tk.X)
        
        # Footer
        self.footer_label = tk.Label(root, text="Discord 스타일 데스크톱 앱", font=("Malgun Gothic", 8), 
                                   fg="#72767d", bg="#36393f", pady=10)
        self.footer_label.pack(side=tk.BOTTOM)

    def on_convert(self):
        input_str = self.input_text.get("1.0", tk.END).strip()
        if not input_str:
            return
            
        converted_str = convert_to_haxyn_style(input_str)
        
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", converted_str)
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = HaxynConverterApp(root)
    root.mainloop()
