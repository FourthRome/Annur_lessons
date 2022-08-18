n = int(input())

seconds = n % 60
minutes = n // 60 % 60
hours = n // 3600 % 24

print(f"{hours}:{minutes:02}:{seconds:02}")
