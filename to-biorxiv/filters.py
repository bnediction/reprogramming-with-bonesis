
def parse_maketitle_mdcell(input):
    data = {
        "addresses": [],
        "abstract": [],
    }
    state = 0
    for line in input.strip().split("\n"):
        line = line.strip()
        # 0. Title
        if state == 0 and line.startswith("# "):
            data["title"] = line[2:].strip()
            state = 1
        # 1. Authors
        elif state == 1 and line:
            line = line.replace("<sup>", "\\,$^{")
            line = line.replace("</sup>", "}$")
            data["authors"] = line
            state = 2
        # 2. Affiliation
        elif state == 2 and line.startswith("> "):
            line = line[2:].replace("<sup>", "$^{").replace("</sup> ", "}$")
            data["addresses"].append(line)
        elif state == 2 and not line:
            state = 3
        # 3,4. Abstract
        elif state == 3 and line == "#### Abstract":
            state = 4
        elif state == 4 and line.startswith("**Keywords**:"):
            data["keywords"] = line.split(":")[1].replace("*","").strip()
            state = 5
            break
        elif state == 4 and line.startswith("> "):
            data["abstract"].append(line[2:].strip())


    data["addresses"] = "\\\\\n".join(data["addresses"])
    data["abstract"] = "\n".join(data["abstract"])
    return data

def latex_metadata(input):
    data = parse_maketitle_mdcell(input)
    return """
\\def\\Title{{{title}}}
\\def\\Authors{{{authors}}}
\\def\\Address{{{addresses}}}""".format(**data)

def abstract(input):
    data = parse_maketitle_mdcell(input)
    return data["abstract"]

def keywords(input):
    data = parse_maketitle_mdcell(input)
    return data["keywords"]

def sup2latex(text):
    return text.replace("<sup>", "$^\\text{").replace("</sup>","}$")


if __name__ == "__main__":
    import sys
    input = sys.stdin.read()
    print(latex_metadata(input))
    print(abstract(input))
    print(keywords(input))

