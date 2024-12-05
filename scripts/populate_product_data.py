import requests as rq
import random

# Globals
domain = "http://localhost:3001"
path = "/"
login_url = domain + "/auth/login/"

common_headers = {"Content-Type": "application/json"}

# Product Creation URI
product_create_url = domain + path

# Authenticating
user_credentials = {"username": "test", "password": "TestTest$1"}

auth_n_res = rq.post(login_url, json=user_credentials, headers=common_headers)

d = auth_n_res.json()
common_headers["Authorization"] = "Token " + d.get("token", "")

### End of Authenticaton

# Data Field Lists
product_names = [
    "Potato",
    "Mango",
    "Cauliflower",
    "Cabbage",
    "Rice",
    "Lentil",
    "Flour",
    "Sugar",
    "Salt",
    "Chickpeas",
    "Pumpkin",
    "Banana",
    "Chilli",
    "Turmeric",
    "Cinnamon",
]

product_categories = [1, 2, 3, 4]

product_images = [
    "https://chaldn.com/_mpimage/deshi-peyaj-local-onion-50-gm-1-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D52358&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/potato-regular-50-gm-1-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D164304&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/lal-peyaj-onion-red-imported-50-gm-1-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D163935&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/potato-regular-25-gm-600-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D164303&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/lal-alu-red-potato-cardinal-50-gm-1-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D76922&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/roshun-garlic-imported-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D89993&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/coriander-leaves-dhonia-pata-10-gm-100-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28562&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kacha-morich-green-chilli-12-gm-250-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28576&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/red-tomato-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D64361&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/potol-pointed-gourd-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D35666&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/boro-alu-big-diamond-potato-50-gm-1-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D79694&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/dheros-ladies-finger-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28563&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/ada-imported-ginger-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D163275&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/lal-shak-red-spinach-1-bundle?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D7226&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/fulkopi-cauliflower-1-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D46971&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kacha-pepe-green-papaya-70-gm-14-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D69930&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/deshi-shosha-local-cucumber-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D64359&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/deshi-gajor-local-carrot-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D64363&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/misti-kumra-fali-sweet-pumpkin-slice-40-gm-1-kg?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28900&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/lomba-lebu-long-lemon-4-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D64362&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kolmi-shak-water-spinach-1-bundle?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28561&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/chichinga-snake-gourd-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28583&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/shosha-cucumber-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D64357&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/borboti-long-bean-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D22410&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/palong-shak-palong-spinach-1-bundle?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28579&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/lomba-kalo-begun-long-brinjal-black-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D43558&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kochur-mukhi-taro-roots-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28965&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/deshi-ada-local-ginger-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D163274&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/gol-lebu-round-lemon-4-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D54834&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/beetroot-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D35682&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/green-capsicum-15-gm-300-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28574&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/badhakopi-cabbage-1-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D5740&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/lau-bottle-gourd-1-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28573&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/korola-bitter-gourd-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D22416&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/deshi-roshun-garlic-local-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D89990&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/premium-koi-fish-500-gm-deshi-roshun-500-gm-combo?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D166138&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/premium-pangas-fish-500-gm-deshi-roshun-500-gm-combo?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D166139&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kacha-kola-banana-green-4-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D83135&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/deshi-peyaj-local-onion-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D163942&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/pui-shak-pui-spinach-1-bundle?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D7071&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/dhundhul-sponge-gourd-20-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D77228&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kagozi-lebu-kagozi-lemon-4-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D43758&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/uchche-local-bitter-gourd-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D15396&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/jali-kumra-water-pumpkin-1-pcs?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D69932&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/sobuj-gol-begun-round-brinjals-green-35-gm-700-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D28795&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/jhinga-ridge-gourd-20-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D120815&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/ada-imported-ginger-25-gm-250-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D163146&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/kochur-loti-stolon-of-taro-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D64498&q=low&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/mula-radish-25-gm-500-gm?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D120817&q=best&v=1&m=400&webp=1",
    "https://chaldn.com/_mpimage/data-shak-data-spinach-1-bundle?src=https%3A%2F%2Feggyolk.chaldal.com%2Fapi%2FPicture%2FRaw%3FpictureId%3D30176&q=low&v=1&m=400&webp=1",
]

unit_names = ["kg", "gram", "n", "liter", "dozon"]

product_descriptions = [
    "This sleek and modern coffee maker brews the perfect cup every time.",
    "Experience ultimate comfort with our ergonomic office chair, designed for long hours of productivity.",
    "Stay connected with our latest smartphone, featuring a stunning display and powerful performance.",
    "Elevate your home decor with this elegant and stylish floor lamp.",
    "Cook like a pro with our non-stick cookware set, perfect for all your culinary adventures.",
    "Keep your beverages hot or cold for hours with our insulated stainless steel tumbler.",
    "Transform your living space with our versatile and durable area rug.",
    "Enjoy crystal-clear sound with our wireless Bluetooth headphones.",
    "Stay organized with our spacious and stylish leather tote bag.",
    "Achieve your fitness goals with our high-quality resistance bands set.",
]

# Performing Product post
for _ in range(50):
    single_product_instance = {
        "product_name": random.choice(product_names),
        "image_url": random.choice(product_images),
        "unit_price": random.randint(20, 500),
        "unit_name": random.choice(unit_names),
        "description": random.choice(product_descriptions),
        "category": random.choice(product_categories),
    }

    rq.post(product_create_url, json=single_product_instance, headers=common_headers)
