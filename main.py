from pdf_reader import extracting_text
from summariser import summarize_text

file=input("Enter PDF path: ")

file=file.strip('"')

pdf_text=extracting_text(file)

print("----- EXTRACTED TEXT -----")
print(pdf_text[:500])

summary=summarize_text(pdf_text)

print("\n----- PDF SUMMARY -----")
print(summary)