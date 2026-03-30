import re

input_file = "ldo.md"
output_file = "ldo_final.md"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Remove caracteres estranhos
text = text.replace("\f", "")

# 2. Normaliza espaços
text = re.sub(r'[ \t]+', ' ', text)

# 3. Corrige quebras de linha no meio de frases
text = re.sub(r'(\w)\n(\w)', r'\1 \2', text)

# 4. Remove excesso de linhas vazias
text = re.sub(r'\n{3,}', '\n\n', text)

lines = text.split("\n")
new_lines = []

for line in lines:
    line = line.strip()

    # Ignora linhas vazias
    if not line:
        new_lines.append("")
        continue

    # TÍTULOS PRINCIPAIS (tudo maiúsculo)
    if line.isupper() and len(line.split()) <= 6:
        new_lines.append(f"\n## {line.title()}\n")
        continue

    # SUBTÍTULOS (palavras importantes)
    if (
        line.istitle()
        and len(line.split()) <= 6
        and not line.endswith(".")
    ):
        new_lines.append(f"\n### {line}\n")
        continue

    # LISTAS (nomes em sequência)
    if line.isupper() and len(line.split()) > 2:
        new_lines.append(f"- {line.title()}")
        continue

    new_lines.append(line)

# Junta tudo
clean_text = "\n".join(new_lines)

# Ajuste final
clean_text = re.sub(r'\n{3,}', '\n\n', clean_text)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(clean_text)

print("Arquivo final gerado: ldo_final.md")