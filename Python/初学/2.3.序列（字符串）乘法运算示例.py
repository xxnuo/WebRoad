# 在位于屏幕中央且宽度合适的方框内打印一个句子

# sentence = input("Sentence: ")
sentence = "these days don't end"
screen_width = 80
text_width = len(sentence)
box_width = text_width +6
left_margin = (screen_width - box_width) // 2

print()
print(' '*left_margin + '+' + '-'*(box_width-2) + '+')
print(' '*left_margin + '|  ' + ' '*text_width  + '  |')
print(' '*left_margin + '|  ' +      sentence   + '  |')
print(' '*left_margin + '|  ' + ' '*text_width  + '  |')
print(' '*left_margin + '+' + '-'*(box_width-2) + '+')
print()
