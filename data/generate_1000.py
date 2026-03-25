import random
import json

categories = {
    "smartphone": {
        "brands": ["Samsung", "OnePlus", "Xiaomi", "Realme"],
        "features": ["camera", "battery", "gaming", "display"],
        "price": (10000, 80000)
    },
    "laptop": {
        "brands": ["HP", "Dell", "Lenovo", "Asus"],
        "features": ["performance", "battery", "lightweight"],
        "price": (30000, 120000)
    },
    "shoes": {
        "brands": ["Nike", "Adidas", "Puma"],
        "features": ["running", "comfort", "durability", "lightweight"],
        "price": (1000, 10000)
    },
    "headphones": {
        "brands": ["Sony", "JBL", "Boat"],
        "features": ["bass", "battery", "noise cancellation"],
        "price": (500, 15000)
    }
}

review_templates = {
    "positive": [
        "Excellent {f}.",
        "Really good {f}.",
        "Very satisfied with {f}.",
        "Great {f} performance.",
        "Worth the price."
    ],
    "neutral": [
        "{f} is okay.",
        "Average {f}.",
        "Decent performance.",
        "Not bad.",
        "Works fine."
    ],
    "negative": [
        "Poor {f}.",
        "Not satisfied with {f}.",
        "Could be better.",
        "Bad experience.",
        "Disappointed."
    ]
}

def generate_reviews(features):
    reviews = []
    sentiments = ["positive"]*3 + ["neutral"]*1 + ["negative"]*1

    for _ in range(5):
        f = random.choice(features)
        sentiment = random.choice(sentiments)
        template = random.choice(review_templates[sentiment])
        reviews.append(template.format(f=f))

    return reviews

def generate_product(i):
    category = random.choice(list(categories.keys()))
    config = categories[category]

    brand = random.choice(config["brands"])
    features = random.sample(config["features"], 2)

    price = random.randint(*config["price"])
    rating = round(random.uniform(3.8, 4.7), 1)

    title = f"{brand} {category} with {features[0]} and {features[1]}"
    description = f"This {category} offers strong {features[0]} and reliable {features[1]}."

    return {
        "id": str(i),
        "category": category,
        "title": title,
        "description": description,
        "price": price,
        "rating": rating,
        "features": features,
        "reviews": generate_reviews(features)
    }

def generate_dataset(n=1000):
    data = [generate_product(i+1) for i in range(n)]

    with open("data/products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"{n} products generated successfully!")

if __name__ == "__main__":
    generate_dataset(1000)