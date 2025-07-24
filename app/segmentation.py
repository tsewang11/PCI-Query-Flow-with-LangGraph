def segment_customer(context):
    # history = context.get("context", "")
    
    # if "buy" in history or "order" in history:
    #     segment = "Returning Customer"
    # elif "discount" in history or "offer" in history:
    #     segment = "Price-Sensitive"
    # else:
    #     segment = "New Customer"
        
        
        
    history = context.get("context", "")
    if "buy" in history or "order" in history:
        segment = "Returning Customer"
    elif "discount" in history or "offer" in history:
        segment = "Price-Sensitive"
    else:
        segment = "New Customer"

    
    return {"segment": segment}
