import re
import spacy

# Load Spacy NLP model
nlp = spacy.load("en_core_web_trf")

class PIIDetector:
    def __init__(self):
        self.patterns = {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "phone": r"\b\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}\b",
            "ssn": r"\b\d{3}[-]?\d{2}[-]?\d{4}\b",
            "ip_address_v4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "ip_address_v6": r"\b(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}\b",
            "hostname": r"\b[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            "uuid": r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
        }

    def scan_file(self, filepath):
        """Scan a file for PII/PHI and save results."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                lines = file.readlines()

            findings = []
            for line_number, line in enumerate(lines, start=1):
                for category, pattern in self.patterns.items():
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        findings.append((category, match.group(), line_number))

                # NLP for detecting names
                doc = nlp(line)
                for ent in doc.ents:
                    if ent.label_ == "PERSON":
                        findings.append(("name", ent.text, line_number))

            result_filename = filepath.replace(".txt", "_results.txt")
            with open(result_filename, "w", encoding="utf-8") as result_file:
                for finding in findings:
                    result_file.write(f"{finding[0]}: {finding[1]} found on line {finding[2]}\n")

            print(f"Results saved in {result_filename}")

        except Exception as e:
            print(f"Error scanning {filepath}: {e}")
