import sys, re, os

sql_path = sys.argv[1]
if not os.path.exists(sql_path):
    print(f"❌ Файл '{sql_path}' не найден.")
    exit(1)

with open(sql_path) as f:
    sql = f.read()

def parse_tables(sql):
    tables = {}
    current_table = None
    buffer = []
    for line in sql.splitlines():
        line = line.strip()
        if line.upper().startswith("CREATE TABLE"):
            match = re.search(r'`(\w+)`', line)
            if match:
                current_table = match.group(1)
                buffer = []
        elif line.startswith(")") and current_table:
            tables[current_table] = "\n".join(buffer)
            current_table = None
        elif current_table:
            buffer.append(line)
    return tables

def parse_columns(definition):
    lines = definition.splitlines()
    columns = []
    fks = []
    for line in lines:
        if line.startswith("`"):
            parts = line.split()
            name = parts[0].strip("`,")
            typ = parts[1]
            null = "NO" if "NOT NULL" in line else "YES"
            default_match = re.search(r"DEFAULT\s+(.*?)(,|\s|$)", line)
            default = default_match.group(1).strip("',`") if default_match else "—"
            columns.append((name, typ, null, default))
        elif "FOREIGN KEY" in line:
            fk_match = re.findall(r"FOREIGN KEY \(`(\w+)`\) REFERENCES `(\w+)` \(`(\w+)`", line)
            if fk_match:
                fks.append(fk_match[0])
    return columns, fks

tables = parse_tables(sql)
output = f"# 📋 Таблицы из `{sql_path}`\n"

for table, definition in tables.items():
    cols, fks = parse_columns(definition)
    output += f"\n## `{table}`\n\n| Поле | Тип | Null | По умолчанию |\n|------|-----|------|---------------|\n"
    for name, typ, null, default in cols:
        output += f"| `{name}` | {typ} | {null} | {default} |\n"
    if fks:
        output += "\n**Связи:**\n"
        for col, ref_table, ref_col in fks:
            output += f"- `{col}` → `{ref_table}.{ref_col}`\n"

with open("tables.md", "w") as f:
    f.write(output)

print("✅ Документация сгенерирована: tables.md")
