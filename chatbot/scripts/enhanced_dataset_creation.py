import random
import json
import os
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for generating realistic data
fake = Faker()

# Business details
business_name = "Tractor Spare Parts.lk"
owner_name = "Thilanka Dilshan"
contact_number = "+94 77 123 4567"
business_email = "tractorsparepartslk.c@gmail.com"
business_hours = "8:00 AM - 6:00 PM (Monday to Saturday)"
emergency_contact = "+94 77 765 4321"

# Expanded lists to create richer variations
tractor_brands = [
    "Massey Ferguson", "John Deere", "New Holland", "Sonalika", "Kubota",
    "Mahindra", "Eicher", "TAFE", "Swaraj", "Escorts", "Case IH", "Claas",
    "Deutz-Fahr", "Yanmar", "Ford", "Fendt", "Valtra", "Steyr", "Same",
    "Lamborghini", "McCormick", "Landini", "Zetor", "Belarus"
]

models = [
    "240", "5050D", "3630", "DI 60", "4710", "6020", "7200", "265 DI", "275 DI",
    "Arjun Novo 605", "Solis 5015", "TX 1610", "Euro 50", "JIVO 245", "410 DI",
    "Major 60", "5100M", "MF 9500", "NH 5630", "MU5501", "MF 8S.305", "JD 6M",
    "NH T9.700", "Kubota M8-211", "Mahindra 475 DI", "Eicher 548", "TAFE 45DI"
]

parts = [
    "clutch plate", "alternator", "engine oil", "air filter", "diesel filter",
    "fuel injector", "hydraulic pump", "radiator", "starter motor", "head gasket",
    "gearbox", "steering pump", "battery", "tyre", "brake shoe", "oil filter",
    "fan belt", "piston ring", "transmission oil", "exhaust manifold",
    "water pump", "differential", "axle", "seat cushion", "front loader",
    "timing belt", "fuel pump", "glow plug", "turbocharger", "injection pump",
    "cylinder head", "crankshaft", "camshaft", "valve spring", "connecting rod",
    "main bearing", "thrust bearing", "oil seal", "gasket set", "fuel tank"
]

# Technical specifications for parts
part_specs = {
    "clutch plate": ["Single/Dual plate", "Ceramic/Metallic", "8/10/12 spline"],
    "alternator": ["12V/24V", "60A/90A/120A", "Internal/External regulator"],
    "engine oil": ["15W-40", "20W-50", "10W-30", "Synthetic/Conventional"],
    "air filter": ["Paper/Cotton", "Single/Dual element", "Standard/Heavy duty"],
    "diesel filter": ["Primary/Secondary", "10/20 micron", "Spin-on/Cartridge"],
    "fuel injector": ["Bosch/Denso/Delphi", "4/6/8 hole", "High/Low pressure"],
    "hydraulic pump": ["Gear/Piston/Vane", "Open/Closed center", "Flow rate: 20-100 LPM"],
    "radiator": ["Aluminum/Copper", "2/3/4 row", "With/Without oil cooler"],
    "starter motor": ["12V/24V", "2.0/2.5/3.0 kW", "Gear reduction/Direct drive"],
    "head gasket": ["Multi-layer steel", "Standard/High compression", "With/Without fire rings"]
}

# Price ranges for parts (min, max)
price_ranges = {
    "clutch plate": (800, 1500),
    "alternator": (3500, 8500),
    "engine oil": (950, 2500),
    "air filter": (450, 1200),
    "diesel filter": (650, 1800),
    "fuel injector": (2500, 7500),
    "hydraulic pump": (8500, 25000),
    "radiator": (4500, 12000),
    "starter motor": (3500, 9000),
    "head gasket": (1200, 3000)
}

warranties = [
    "6-month", "1-year", "3-month", "2-year", "18-month", "9-month",
    "5-year", "4-year", "Lifetime"
]

locations = [
    "Anuradhapura", "Colombo", "Kandy", "Galle", "Jaffna",
    "Kurunegala", "Matara", "Negombo", "Ratnapura", "Polonnaruwa",
    "Batticaloa", "Trincomalee", "Badulla", "Chilaw", "Vavuniya",
    "Monaragala", "Kalutara", "Puttalam", "Nuwara Eliya", "Hambantota"
]

actions = [
    "buy", "order", "replace", "repair", "inquire about", "check availability of",
    "get price for", "find", "confirm compatibility for", "book",
    "schedule installation of", "return", "exchange", "warranty claim for",
    "maintenance of", "upgrade", "downgrade", "compare prices for"
]

# Customer scenarios
customer_scenarios = [
    "emergency repair needed",
    "regular maintenance",
    "upgrading old parts",
    "new tractor purchase",
    "warranty claim",
    "seasonal preparation",
    "after accident repair",
    "performance improvement",
    "cost optimization",
    "preventive maintenance"
]

# Seasonal variations
seasons = ["dry season", "rainy season", "harvest season", "planting season"]

# Discount scenarios
discounts = {
    "bulk_purchase": (5, 15),  # 5-15% for bulk
    "seasonal": (10, 25),      # 10-25% seasonal
    "loyalty": (5, 10),        # 5-10% for loyal customers
    "emergency": (0, 5)        # 0-5% for emergency repairs
}

def generate_price(part, scenario=None):
    min_price, max_price = price_ranges.get(part, (1000, 5000))
    base_price = random.randint(min_price, max_price)
    
    if scenario:
        if scenario == "bulk_purchase":
            discount = random.randint(*discounts["bulk_purchase"])
        elif scenario == "seasonal":
            discount = random.randint(*discounts["seasonal"])
        elif scenario == "loyalty":
            discount = random.randint(*discounts["loyalty"])
        else:
            discount = 0
        return base_price * (1 - discount/100)
    return base_price

def generate_follow_up_question(instruction, response):
    follow_up_templates = [
        "What's the installation cost?",
        "Do you offer any warranty?",
        "How long will delivery take?",
        "Can I get a discount for bulk purchase?",
        "Do you have any other compatible parts?",
        "What's the return policy?",
        "Can you recommend a good mechanic?",
        "Do you offer installation service?",
        "What payment methods do you accept?",
        "Can I get a detailed quote?"
    ]
    return random.choice(follow_up_templates)

def generate_follow_up_response(instruction, response, follow_up):
    follow_up_responses = [
        f"Installation costs Rs. {random.randint(500, 2000)}. We can schedule it within {random.randint(1, 3)} days.",
        f"Yes, all parts come with a {random.choice(warranties)} warranty.",
        f"Delivery to your location takes {random.randint(1, 5)} business days.",
        f"Yes, we offer {random.randint(5, 15)}% discount on bulk purchases.",
        f"Yes, we have several compatible parts. Would you like me to list them?",
        f"Our return policy allows returns within {random.randint(7, 30)} days if the part is unused.",
        f"Yes, we work with certified mechanics. I can provide their contact details.",
        f"Yes, we offer installation service for Rs. {random.randint(1000, 3000)}.",
        f"We accept cash, credit cards, and bank transfers.",
        f"I'll prepare a detailed quote and send it to your email."
    ]
    return random.choice(follow_up_responses)

def generate_data_point():
    brand = random.choice(tractor_brands)
    model = random.choice(models)
    part = random.choice(parts)
    scenario = random.choice(customer_scenarios)
    season = random.choice(seasons)
    price = generate_price(part, scenario)
    warranty = random.choice(warranties)
    location = random.choice(locations)
    action = random.choice(actions)
    
    # Get technical specifications if available
    specs = part_specs.get(part, ["Standard specification"])
    spec = random.choice(specs)

    # Instruction templates with more variety
    instruction_templates = [
        f"Do you have a {part} for {brand} {model}?",
        f"I want to {action} a {part} for my {brand} {model}.",
        f"Is the {part} compatible with {brand} {model}?",
        f"How much is the {part} for {brand} {model}?",
        f"Can you recommend a good {part} for {brand} {model}?",
        f"Do you deliver parts to {location}?",
        f"Where can I get a {part} for {brand} {model}?",
        f"Can I {action} a {part} for {brand} {model} from your store?",
        f"I'm looking to {action} a {part} for {brand} {model}.",
        f"Is the {part} available for {brand} {model} and can you ship to {location}?",
        f"I need a {part} for {brand} {model} urgently due to {scenario}.",
        f"What's the best {part} for {brand} {model} during {season}?",
        f"Can you tell me the specifications of the {part} for {brand} {model}?",
        f"I'm experiencing issues with my {part} on {brand} {model}. What should I do?",
        f"Do you have the {spec} version of {part} for {brand} {model}?"
    ]
    instruction = random.choice(instruction_templates)

    # Response templates with more context
    response_templates = [
        f"Yes, we have {part}s compatible with {brand} {model}. The {spec} version costs Rs. {price} and comes with a {warranty} warranty. I'm {owner_name} from {business_name}. Feel free to call us at {contact_number} or email us at {business_email}.",
        f"The {part} for {brand} {model} is available at Rs. {price}. We're open {business_hours}. You can contact {business_name} at {contact_number} or email {business_email} to place an order.",
        f"Yes, we deliver to {location}. Delivery charges and timelines will be shared once your order is confirmed. For urgent deliveries, call {emergency_contact}.",
        f"For {brand} {model}, we recommend our high-quality {part} ({spec}) priced at Rs. {price}. Contact {business_name} on {contact_number} or via email at {business_email} for more info.",
        f"Currently, the {part} for {brand} {model} is out of stock at {business_name}. Expected restock in {random.randint(1, 7)} days. You can call {contact_number} to pre-order.",
        f"We have several options for {part}s compatible with {brand} {model}. The {spec} version starts at Rs. {price}. I'm {owner_name}. Call {contact_number} or email {business_email} to know more.",
        f"The {part} comes with a {warranty} warranty and costs Rs. {price}. For {scenario}, we recommend regular maintenance every {random.randint(3, 6)} months.",
        f"We can arrange delivery of the {part} for {brand} {model} to {location} within {random.randint(1, 3)} business days. For arrangements, please call {contact_number}.",
        f"Yes, the {part} fits the {brand} {model}. The {spec} version costs Rs. {price}. You can reach {business_name} on {contact_number} or email {business_email} to place your order.",
        f"Unfortunately, the {part} for {brand} {model} is not in stock right now at {business_name}. Please call {contact_number} or email {business_email} and we can notify you when it's available."
    ]
    response = random.choice(response_templates)

    # Generate follow-up question and response
    follow_up = generate_follow_up_question(instruction, response)
    follow_up_response = generate_follow_up_response(instruction, response, follow_up)

    return {
        "instruction": instruction,
        "response": response,
        "follow_up": follow_up,
        "follow_up_response": follow_up_response,
        "metadata": {
            "brand": brand,
            "model": model,
            "part": part,
            "specification": spec,
            "price": price,
            "warranty": warranty,
            "location": location,
            "scenario": scenario,
            "season": season
        }
    }

def main():
    # Generate dataset
    dataset = [generate_data_point() for _ in range(1000000)]

    # Create output directory if it doesn't exist
    output_path = 'data/raw/enhanced_tractor_parts_chatbot_dataset.json'
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    # Save to JSON file
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)

    print(f"✅ Dataset generated and saved at: {output_path}")
    print("Total records:", len(dataset))
    print("\nDataset includes:")
    print("- Follow-up questions and responses")
    print("- Technical specifications")
    print("- Seasonal variations")
    print("- Customer scenarios")
    print("- Price variations based on scenarios")
    print("- Emergency contact information")
    print("- Business hours")
    print("- Detailed metadata for each conversation")

if __name__ == "__main__":
    main() 