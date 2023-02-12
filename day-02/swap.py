"""Text = “created my first program in research zlight”      
Replace the text “first” to “second”Swap the words research and zlight
Displayed as”Created my second program in Zlight Research Pvt Ltd”."""


Text0 = 'created my first program in research zlight'
Text1='pvt Ltd'
# add new string "pvt Ltd"
Text=" ".join([Text0,Text1]) 
#replace first to second 
x=Text.replace('first','second')
print(x)