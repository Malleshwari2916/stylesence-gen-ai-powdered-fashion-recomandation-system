def product_recommendation(skin_tone):
    products = {
        "Fair": ["Pastel shirts", "Light blue jeans"],
        "Medium": ["Earth tone jackets", "Olive shirts"],
        "Dark": ["Bright colors", "White outfits"]
    }
    return products.get(skin_tone, [])
