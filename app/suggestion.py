def generate_suggestion(segment_data):
    segment = segment_data.get("segment", "")
    
    suggestions = {
        "New Customer": "Welcome! You can try our starter pack with 10% off.",
        "Returning Customer": "Thanks for coming back! Here’s a loyalty bonus.",
        "Price-Sensitive": "We’ve got a special 20% discount just for you."
    }
    
    return {"suggestion": suggestions.get(segment, "Let us know how we can help.")}
