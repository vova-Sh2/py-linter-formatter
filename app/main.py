def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(f) for f in errors],
        "path": file_path,
        "status": "failed" if not errors == [] else "passed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [format_linter_error(f) for f in linter_report[i]],
            "path": i,
            "status": "failed" if not linter_report[i] == [] else "passed"
        }
        for i in linter_report
    ]
