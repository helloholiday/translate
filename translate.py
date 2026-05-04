import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        return

    try:
        result = GoogleTranslator(source='auto', target='zh-CN').translate(input_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {e}")

# 创建窗口
root = tk.Tk()
root.title("翻译工具")

# ⭐ 关键1：固定窗口大小
root.geometry("400x300+0+0")   # +0+0 = 左上角

# ⭐ 关键2：始终置顶
root.attributes("-topmost", True)

# ⭐ 可选：禁止调整大小（更像工具栏）
root.resizable(False, False)

# 输入框
tk.Label(root, text="输入内容：").pack()

input_box = tk.Text(root, height=6)
input_box.pack()

# 按钮
tk.Button(root, text="翻译", command=translate_text).pack(pady=5)

# 输出框
tk.Label(root, text="翻译结果：").pack()

output_box = tk.Text(root, height=6)
output_box.pack()

root.mainloop()