def censor(text, word):
  result = [] 
  text = text.split()
  for sub in text:
    if sub == word:
      result.append(len(word)* "*") 
    else:
      result.append(sub) 
  return " ".join(result) 


print(censor("this hack is wack hack", "hack"))