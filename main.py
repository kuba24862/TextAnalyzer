import analyzer

text = open("text.txt", "r")
textnejede = analyzer.TextAnalyzer(text.read())

print(textnejede)
