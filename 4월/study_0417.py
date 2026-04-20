scores = [(80,100),
          (100,50),
          (70,100), (80,90)]

scores.sort(key=lambda x: (-x[0],-x[1])) # 영어로 내림차순, 같으면 수학내림차순

for s in scores:
    print(f"english={s[0]}, math={s[1]}")