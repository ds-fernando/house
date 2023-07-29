from flask import Flask, render_template
app=Flask(__name__)


#Rutas 
@app.route('/')
def inicio ():
    return render_template('sitio/index.html')


@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/iniciar sesión')
def sesión():
    return render_template('sitio/login.html')



##Rutas Admin

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin')
def admin_login():
    return render_template('admin/login.html')



if __name__== '__main__':
    app.run(debug=True)


