
def read_rows(lines):
    rows = []
    headers = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        fields = [field.strip() for field in line.split(",")]

        if headers is None:
            headers = fields
            continue

        if len(fields) != len(headers):
            continue

        rows.append(dict(zip(headers, fields)))

    return rows


def count_types(rows):
    counts = {}

    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1

    return counts


def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row["тип"] != kind:
            continue

        value = row["минуты"].replace(",", ".")

        try:
            total += float(value)
        except ValueError:
            continue

    return round(total, 1)


def to_csv(counts):
    lines = ["тип,количество"]

    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")

    return "\n".join(lines) + "\n"