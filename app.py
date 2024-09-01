from flask import Flask, request, redirect

app = Flask(__name__)

# Define your app URLs
play_store_url = "https://play.google.com/store/apps/details?id=com.init.seaberry"
app_store_url = "https://apps.apple.com/in/app/seaberry-foods/id1606602722"
website_url = "https://seaberryonline.com/home"

@app.route('/dynamic-link')
def dynamic_link():
    user_agent = request.headers.get('User-Agent').lower()

    if 'android' in user_agent:
        return redirect(play_store_url)
    elif 'iphone' in user_agent or 'ipad' in user_agent:
        return redirect(app_store_url)
    else:
        return redirect(website_url)

if __name__ == '__main__':
    app.run(debug=True)
