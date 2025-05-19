def classify_accounts(profile_data):
    classified = []

    for profile in profile_data:
        bio = profile["bio"].lower()

        if "reparación" in bio or "servicio" in bio:
            acc_type = "Repair Shop"
        elif "mayoreo" in bio or "distribuidor" in bio:
            acc_type = "Distributor"
        elif "venta" in bio or "celulares" in bio:
            acc_type = "Retailer"
        else:
            acc_type = "Reseller"

        profile["type"] = acc_type
        classified.append(profile)

    return classified
