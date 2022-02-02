from flask import Flask, render_template, redirect, request
def teen_value(num):
    if num >12 and num< 20 and num!=15 and num!=16:
        return 0
    else:
        return num

def teen_sum(a,b,c):
    return teen_value(a)+teen_value(b)+teen_value(c)

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def home():
    if request.method == "POST":
        try:
            a= int(request.form.get('num1'))
            b =int(request.form.get('num2'))
            c= int(request.form.get('num3'))
            add=teen_sum(a,b,c)
            return render_template('result.html', add=add)
        
        except ValueError:
            return render_template('result.html', add='All inputs must be numeric.')

        except IndexError:
            return render_template('result.html', add="Exactly 3 numbers are required.")
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
