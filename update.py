@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = None
    products = None

    if request.method == 'POST':
        image = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)

        skin_tone = detect_skin_tone(path)
        recommendation = get_style_recommendation(skin_tone)
        products = product_recommendation(skin_tone)

    return render_template(
        'index.html',
        recommendation=recommendation,
        products=products
    )
