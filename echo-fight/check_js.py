import os

def check():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tag = '<script>'
    end_tag = '</script>'
    
    start_idx = content.find(start_tag)
    # Find the last script tag usually
    last_end_idx = content.rfind(end_tag)
    
    if start_idx == -1 or last_end_idx == -1:
        print("Could not find script tags")
        return
        
    # Find the start tag and everything after it
    # Note: index.html has multiple script tags in <head>.
    # We want the main one at the bottom.
    
    scripts = []
    curr = 0
    while True:
        s = content.find('<script>', curr)
        if s == -1: break
        e = content.find('</script>', s)
        if e == -1: break
        scripts.append(content[s+len('<script>'):e])
        curr = e + len('</script>')
    
    print(f"Found {len(scripts)} script blocks.")
    
    for i, js in enumerate(scripts):
        with open(f'debug_{i}.js', 'w', encoding='utf-8') as f:
            f.write(js)
        print(f"Checking debug_{i}.js...")
        res = os.system(f'node --check debug_{i}.js')
        if res != 0:
            print(f"!!! Error in block {i}")
        else:
            print(f"Block {i} OK")

if __name__ == "__main__":
    check()
