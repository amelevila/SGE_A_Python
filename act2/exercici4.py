salari = 20000
if salari<15000:
    print(f"Salari inicial: {salari}")
    print(f"Salari després de IVA: {salari}")
elif salari<30000:
    print(f"Salari inicial: {salari}")
    salari += salari*0.1
    print(f"Salari després de IVA: {salari}")
elif salari<60000:
    print(f"Salari inicial: {salari}")
    salari += salari*0.21
    print(f"Salari després de IVA: {salari}")