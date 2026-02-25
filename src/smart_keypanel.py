def generate_key_value_panel(entities, doc_type=None):
    panel = {}

    if doc_type:
        panel["Document Type"] = doc_type

    def pick(key):
        return entities.get(key, [""])[0] if entities.get(key) else ""

    panel["Invoice Number"] = pick("INVOICE_NUMBER")
    panel["Order Number"] = pick("ORDER_NUMBER")
    panel["Date"] = pick("INVOICE_DATE") or pick("ORDER_DATE") or pick("DATE")
    panel["Amount"] = pick("MONEY")
    panel["Company / Org"] = pick("ORG")
    panel["Person"] = pick("PERSON")
    panel["Address"] = pick("ADDRESS")
    panel["GSTIN"] = pick("GST")
    panel["PAN"] = pick("PAN")
    panel["CIN"] = pick("CIN")

    return panel