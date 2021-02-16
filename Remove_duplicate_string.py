# Remove duplicates from the String

s='ggghhhdddeghytsdefdjgalnbyh'
result=''
for ch in s:
    if ch not in result:
        result=result+ch
print(result)

# Time complexity O(n)
# space complexity O(n) because of taking result as string
