import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100  # cm를 m로 변환
        weight = float(entry_weight.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            status = "저체중"
        elif 18.5 <= bmi < 24.9:
            status = "정상"
        elif 25 <= bmi < 29.9:
            status = "과체중"
        else:
            status = "비만"

        label_result.config(text=f"BMI: {bmi}\n상태: {status}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")

window = tk.Tk()
window.title("BMI 계산기")

# 키 입력
label_height = tk.Label(window, text="키 (cm):")
label_height.grid(column=0, row=0, padx=10, pady=10)

entry_height = tk.Entry(window)
entry_height.grid(column=1, row=0, padx=10, pady=10)

# 몸무게 입력
label_weight = tk.Label(window, text="몸무게 (kg):")
label_weight.grid(column=0, row=1, padx=10, pady=10)

entry_weight = tk.Entry(window)
entry_weight.grid(column=1, row=1, padx=10, pady=10)

# 계산 버튼
button_calculate = tk.Button(window, text="BMI 계산", command=calculate_bmi)
button_calculate.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# 결과 출력
label_result = tk.Label(window, text="BMI: \n상태: ")
label_result.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

window.mainloop()