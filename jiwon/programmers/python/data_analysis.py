def solution(data, ext, val_ext, sort_by):
    standard = ["code", "date", "maximum", "remain"]
    data = [item for item in data if item[standard.index(ext)] < val_ext]
    return sorted(data, key=lambda x: x[standard.index(sort_by)])

