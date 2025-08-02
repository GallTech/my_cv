import json

with open("cv.json") as f:
    data = json.load(f)

with open("cv.tex", "w") as tex:
    tex.write(r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{titlesec}
\titleformat{\section}{\large\bfseries}{}{0em}{}
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}

\begin{document}
""")

    tex.write(f"\\begin{{center}}\n\\LARGE\\textbf{{{data['name']}}} \\\\[0.2cm]\n")
    tex.write(f"\\normalsize {data['title']} \\\\ \n\\end{{center}}\n\n")

    tex.write("\\section*{Experience}\n")
    for job in data["experience"]:
        tex.write(f"\\textbf{{{job['role']}}}, {job['company']} \\hfill {job['years']}\\\\\n")

    tex.write("\n\\end{document}")
