import re
print("Enter/Paste your the model summary. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
state = 0
with open("generated.txt","w") as fout:
    for index, line in enumerate(contents):
        if index == 0:
            fout.write("\\begin{table}[!htb]\n")
            print("Enter table caption")
            caption = input()
            fout.write("\caption{%s}\n" %caption)
            fout.write("\\begin{center}\n\\begin{tabular}{ccc}\n\\toprule")
            fout.write("\multicolumn{1}{c}{Layer} & \multicolumn{1}{c}{Output Shape} & \multicolumn{1}{c}{Params}\\\\\n\midrule\n")
        if "=" in line:
            state += 1
        if state == 1 and "__" not in line and "=" not in line:
            l = re.findall(r"\w+ \(\w+[\)| ]",line)[0].replace("_","\_")
            o = re.findall(r"\(\w+, \)|\(\w+, \w+\)|\(\w+, \w+, \w+\)|\(\w+, \w+, \w+, \w+\)|\(\w+, \w+, \w+, \w+, \w+\)",line)[0]
            p = re.findall(r" [0-9]+ ",line)[0]
            fout.write("{} & {} & {} \\\\\n\midrule\n".format(l,o,p))
        if state == 2 and "_" not in line and "=" not in line:
            row = line.split(": ")
            fout.write(("\\textbf{%s} & & %s \\\\\n\midrule\n" % (row[0],row[1])) if index < len(contents) - 2 else ("\\textbf{%s} & & %s \\\\\n\\bottomrule\n" % (row[0],row[1])))
        if index == (len(contents) - 1):
            fout.write("\end{tabular}\n\end{center}\n\end{table}")






