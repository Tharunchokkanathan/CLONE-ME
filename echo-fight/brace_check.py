def check_braces():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tag = '<script>'
    end_tag = '</script>'
    
    start_idx = content.rfind('<script>') # Get the main logic script
    end_idx = content.find(end_tag, start_idx)
    
    js = content[start_idx+len('<script>'):end_idx]
    
    stack = []
    lines = js.split('\n')
    for i, line in enumerate(lines):
        for char in line:
            if char == '{':
                stack.append(i+1)
            elif char == '}':
                if not stack:
                    print(f"Extra closing brace at line {i+1} of script")
                else:
                    stack.pop()
    
    if stack:
        print(f"Unclosed braces starting at lines: {stack}")
    else:
        print("Braces are balanced!")

if __name__ == "__main__":
    check_braces()
