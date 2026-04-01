from style_converter import convert_to_haxyn_style

test_cases = [
    "아니 정말 내가 오늘 디코를 하다가 12년생 여자애 한 명하고 대화하고 있었는데",
    "걔가 공부가 너무 어렵다고 하더라고",
    "대답은 해줘야 할 것 같아서",
    "공부를 더 열심히 해",
    "미안하다고 사과했고",
    "좋아해",
    "응 알겠어"
]

print("--- haxyn._.s2 Style Conversion Test ---")
for case in test_cases:
    print(f"Original: {case}")
    print(f"Converted: {convert_to_haxyn_style(case)}")
    print("-" * 30)
