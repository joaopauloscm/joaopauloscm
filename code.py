def pad(text, width):
	return text + ' ' * (width - len(text))
profile = [
	"João Paulo Pereira Santana",
	"Computer Science Student",
	"Focus: Data — SQL • MySQL • Python"
]
stack = [
	("[data]",      "MySQL • SQL • Database Modeling • ETL"),
	("[code]",      "Python • Git & GitHub • Terminal"),
	("[building]",  "olist-sql-analysis — e-commerce data, MySQL"),
	("[shipped]",   "amazon-reviews ETL — normalized DB (team)"),
	("[next]",      "Window Functions • Metabase • dbt")
]
goals = [
	"Ship one finished data project at a time",
	"Grow a portfolio recruiters can verify",
	"Land a data analyst / analytics role",
	"Use Python as my data toolkit"
]
status = "Building olist-sql-analysis in MySQL."
width = 63
border = "┌" + "─" * (width - 2) + "┐"
sep    = "├" + "─" * (width - 2) + "┤"
footer = "└" + "─" * (width - 2) + "┘"
def print_centered(text):
	print("│ " + text.center(width - 4) + " │")
print(border)
for line in profile:
	print_centered(line)
print(sep)
for key, value in stack:
	print(f"│ {pad(key, 13)} {pad(value, width - 18)} │")
print(sep)
print("│ Goals:" + " " * (width - 9) + "│")
for g in goals:
	print(f"│   • {pad(g, width - 7)}│")
print(sep)
print_centered(f"Status: {status}")
print(footer)
