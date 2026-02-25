import re
import difflib
from collections import defaultdict

def extract_entities(text: str) -> dict:

    entities = defaultdict(list)

    lines = [l.strip() for l in text.splitlines() if l.strip()]


    for line in lines:
        if (
            line.isupper() 
            and len(line.split()) >= 2
            and not any(char.isdigit() for char in line)
            and len(line) <= 60
        ):
            entities["ORG"].append((line, 0.95))   # confidence


    name_markers = ["to:", "bill to", "ship to", "recipient", "sold to", "customer"]

    for line in lines:
        l = line.lower()

        for marker in name_markers:
            if marker in l:
                parts = line.replace("—", ":").replace("-", ":").split(":")
                if len(parts) > 1:
                    name = parts[1].strip()
                    name = re.split(r"\b[A-Z]{3,}\b", name)[0].strip()
                    name = " ".join([w for w in name.split() if not w.isupper()])

                    if (
                        name 
                        and not any(ch.isdigit() for ch in name) 
                        and 2 <= len(name.split()) <= 4
                    ):
                        entities["PERSON"].append((name, 0.92))

    date_patterns = [
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",  
        r"\b\d{1,2}[/-][A-Za-z]{3}[/-]\d{2,4}\b", 
        r"\b[A-Za-z]{3,9} \d{1,2}, \d{4}\b",
        r"\b\d{4}\b"
    ]

    for pat in date_patterns:
        for m in re.findall(pat, text):
            entities["DATE"].append((m, 0.85))

    for line in lines:
        if difflib.SequenceMatcher(None, line.lower(), "invoice date").ratio() > 0.6:
            possible_date = re.findall(r"[A-Za-z0-9/:-]+", line)
            if len(possible_date) > 1:
                entities["INVOICE_DATE"].append((possible_date[-1], 0.95))

    money_patterns = [
        r"(₹|Rs\.?|INR)\s?\d{1,3}(?:,\d{3})*(?:\.\d+)?",
        r"\d{1,3}(?:,\d{3})+\.\d+",
    ]

    for pat in money_patterns:
        for m in re.findall(pat, text):
            entities["MONEY"].append((m, 0.97))

    for line in lines:
        if difflib.get_close_matches("invoice", line.lower().split(), cutoff=0.6):
            match = re.findall(r"[A-Z0-9-]+", line)
            if match:
                entities["INVOICE_NUMBER"].append((match[-1], 0.9))

        if difflib.get_close_matches("order", line.lower().split(), cutoff=0.6):
            match = re.findall(r"[A-Z0-9-]+", line)
            if match:
                entities["ORDER_NUMBER"].append((match[-1], 0.88))

    address_candidates = []
    for line in lines:
        if (
            "," in line 
            or re.search(r"\d{3,6}", line) 
            or any(w in line.lower() for w in ["street", "road", "nagar", "colony", "city", "state"])
        ):
            address_candidates.append(line)

    if address_candidates:
        full_address = " ".join(address_candidates)
        entities["ADDRESS"].append((full_address, 0.75))

    pan = re.findall(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b", text)
    for p in pan:
        entities["PAN"].append((p, 0.99))

    gst = re.findall(r"\b[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][A-Z0-9]Z[A-Z0-9]\b", text)
    for g in gst:
        entities["GST"].append((g, 0.98))

    cin = re.findall(r"\b[LU][0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}\b", text)
    for c in cin:
        entities["CIN"].append((c, 0.97))

    final_entities = {}

    for key, values in entities.items():
        cleaned = []
        for val, conf in values:
            if val not in cleaned:
                cleaned.append((val, conf))

        final_entities[key] = cleaned
    return final_entities