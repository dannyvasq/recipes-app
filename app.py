
# Import neccesary libraries and modules

from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime


# Initialize Flask app and configure database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Define User model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)


# Define Recipe model

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Load user function for Flask_Login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route to show all recipes

@app.route('/')
@app.route('/recipes')
def show_recipes():
    recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=recipes)


# Route to add a new recipe

@app.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            author=current_user
        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!', 'success')
        return redirect(url_for('show_recipes'))
    return render_template('new_recipe.html', form=form)


# Route to show recipe details

@app.route('/recipe/<int:id>')
def recipe_details(id):
    recipe = Recipe.query.get_or_404(id)
    return render_template('recipe_details.html', recipe=recipe)


# Route to delete a recipe

@app.route('/recipe/<int:id>/delete', methods=['POST'])
@login_required
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if recipe.author != current_user:
        flash('You do not have permission to delete this recipe.', 'danger')
        return redirect(url_for('show_recipes'))
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('show_recipes'))


# Route to login

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('show_recipes'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


# Route to logout

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('show_recipes'))


# Route to register a new user

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# Run the Flask app

if __name__ == '__main__':
    app.run(debug=True)




